#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : python_server.py
__time__    : 2020/6/15 23:10
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""
import requests


def http_server(args_url):
    r = requests.get(url=args_url)
    print("r.headers: ", r.headers)
    print("服务器中间件为: ", r.headers["Server"])


if __name__ == "__main__":
    base_url = "http://127.0.0.1:8888/"
    http_server(args_url=base_url)
