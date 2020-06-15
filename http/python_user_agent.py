#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : python_user_agent.py
__time__    : 2020/6/15 22:45
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import requests


def http_python_user_agent(args_url):
    r = requests.get(url=args_url)
    print("python_user_agent: ", r.request.headers)


def http_define_user_agent(args_url, args_headers):
    r = requests.get(url=args_url, headers=args_headers)
    print("define_user_agent: ", r.request.headers)


if __name__ == "__main__":
    base_url = "https://www.baidu.com/"
    base_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }

    http_python_user_agent(args_url=base_url)

    http_define_user_agent(args_url=base_url, args_headers=base_headers)
