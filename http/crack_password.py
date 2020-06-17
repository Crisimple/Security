#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : crack_password.py
__time__    : 2020/6/17 14:42
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import  optparse

# 初始化对象
parser = optparse.OptionParser()

# 初始化对象的 usage 属性
parser.usage = "crack_password.py -u user_file"

# 添加参数
parser.add_option(
    "-u", "--user_file",
    help="read username from file",
    action="store",
    type="string",
    metavar="FILE",
    dest="username_file"
)

# 存储提交的命令行参数
(options, args) = parser.parse_args()

# 测试数据
print(options.username_file)