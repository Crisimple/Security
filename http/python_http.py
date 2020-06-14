#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : python_http.py
__time__    : 2020/6/14 17:35
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""
import requests


def get_no_params(arg_url):
    r = requests.get(arg_url)
    print("请求的URL：", r.url)
    print("请求的状态码：", r.status_code)

def get_params(arg_url, arg_payload):
    r = requests.get(url=arg_url, params=arg_payload)
    print("请求的URL：", r.url)
    print("请求的状态码：", r.status_code)
    print("请求响应文本：", r.content)

def post_data(arg_url, arg_data):
    r = requests.post(url=arg_url, data=arg_data)
    print()


if __name__ == "__main__":
    get_no_params_url = "https://httpbin.org"
    # get_no_params(arg_url=get_no_params_url)

    get_params_url = "http://httpbin.org/#/Auth/get_basic_auth__user___passwd_"
    base_arg_payload = {
        "username": "test",
        "password": "123456"
    }

    get_params(arg_url=get_params_url, arg_payload=base_arg_payload)