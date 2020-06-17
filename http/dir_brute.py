#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : dir_brute.py
__time__    : 2020/6/16 22:22
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""
import getopt
import sys
import math
import threading
import requests

def banner():
    print("*"*30)
    print("*"*5 + " "*4 + "DirBrute v1.0" + " "*3 + "*"*5)
    print("*"*30)
    print("This tool just develop for education!")


def usage():
    print("This's the tool's usage.")
    print("python dir_brute.py -u url -t threads -d dictionary")

# opts, args = getopt.getopt(sys.argv[1:], "u:t:d:")
# print("type(opts): ", type(opts))
# print("opts: ", opts)
# print("type(args): ", type(args))
# print("args: ", args)
# for k, v in opts:
#     print(k)
#     print(v)

def multi_scan(args_url, args_threads, args_dic):
    """
    :param args_url: 进行爆破的目标网站
    :param args_threads: 爆破读取文件字典的线程数
    :param args_dic: 爆破使用的字典文件
    :return: 每个线程读取的爆破目录
    :description: (1) 读取字典文件；（2）确定读取的行数；（3）制作每一个线程读取的字典列表[[t1], [t2], [t3]]
    """
    result_list = []
    threading_list = []
    with open(args_dic, "r", encoding="utf-8") as f:
        # 读取字典文件所有行
        dict_list = f.readlines()
        # 计算每个线程要读取字典文件的个数
        if len(dict_list) % int(args_threads) == 0:
            thread_read_line_num = len(dict_list) / int(args_threads)
        else:
            thread_read_line_num = math.ceil(len(dict_list) / int(args_threads))

        i = 0
        temp_list = []
        for line in dict_list:
            i += 1
            if i % thread_read_line_num == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list =[]
            else:
                temp_list.append(line.strip())

        for i in result_list:
            threading_list.append(threading.Thread(target=scan, args=(args_url, i)))
        for t in threading_list:
            t.start()

def scan(args_url, dic):
    """
    :param args_url: 要扫描的网站
    :param args_dic: 字典文件
    :return:
    """
    # 实现扫描功能
    for line in dic:
        # print("line: ", line)
        r = requests.get(args_url + "/" + line)
        if r.status_code == 200:
            # print("r.url: ", r.url + line)
            print(r.url + ": " + str(r.status_code))


def start():
    if len(sys.argv) == 7:
        opts, args = getopt.getopt(sys.argv[1:], "u:t:d:")
        for k, v in opts:
            print("k: ", k)
            print("v: ", v)
            if k == "-u":
                url = v
            elif k == "-t":
                threads = v
                # print("threads: " + threads)
            elif k == "-d":
                dictionary = v
        # print("url: " + url)
        # print("threads: " + threads)
        # print("dictionary: " + dictionary)
        multi_scan(url, threads, dictionary)
    else:
        print("Error Arguments.")
        sys.exit()

if __name__ == "__main__":
    # banner()
    # usage()
    # start()

    base_url = "http://127.0.0.1:8888"
    base_file = "../data/scan_dir.txt"
    multi_scan(base_url, 5, base_file)
    #
    # base_dic = "../da"
    # scan(args_url=base_url, args_dic="../")
    # scan(args_url=base_url, args_dic=base_dic)