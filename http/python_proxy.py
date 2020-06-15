#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : python_proxy.py
__time__    : 2020/6/14 20:10
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description: http proxy shark bag
通过在python requests 中设置与 BurpSuite 相同的代理地址，启动监听来抓取数据包
"""

import requests

def http_proxy(args_url, args_proxies):
    r = requests.get(
        url=args_url,
        proxies=proxies,
        verify=False
    )
    print(r.status_code)

if __name__ == "__main__":
    base_url = "https://www.baidu.com"
    proxies = {
        "http": "127.0.0.1:8080",
        "https": "127.0.0.1:8080"
    }
    http_proxy(args_url=base_url, args_proxies=proxies)