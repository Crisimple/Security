#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : scan_dir.py
__time__    : 2020/6/15 21:38
__author__  : crisimple
暴力破解文件目录

可以在本地起一个简单的python http 服务：
    python -m http.server 8888
"""

import requests
import sys

def scan_dir(args_url, args_file):

    with open(args_file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            r = requests.get(args_url + line)
            if r.status_code == 200:
                print("url: " + r.url + " exists.")


if __name__ == "__main__":
    base_url_arg = sys.argv[1]
    base_url = "http://127.0.0.1:8888/"
    base_file = "../data/scan_dir.txt"
    scan_dir(args_url=base_url_arg, args_file=base_file)
