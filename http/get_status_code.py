#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : get_status_code.py
__time__    : 2020/6/14 16:30
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import requests

base_url = "https://httpbin.org"

def get_status_code():
    response = requests.get(base_url)
    status_code = response.status_code
    return status_code


print(get_status_code())
