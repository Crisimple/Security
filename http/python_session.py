#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : python_session.py
__time__    : 2020/6/15 21:24
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import requests

def http_session(args_url):
    rs = requests.Session()
    r = rs.get(args_url)
    r1 = rs.get(args_url)
    print(r.cookies)
    print(r.request.headers)
    print(r1.request.headers)


if __name__ == "__main__":
    base_url = "https://www.baidu.com/"
    http_session(args_url=base_url)
