#!/usr/bin/env python

# 正则表达式, 简称为regex, 是文本模式的描述方法

import re

# 向 re.compile() 传入一个字符串值, 表示正则表达式, 它将返回一个 Regex 模式对象
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# Regex 对象的 search() 方法查找传入的字符串, 寻找该正则表达式的所有匹配
# 如果字符串中没有找到该正则表达式模式, search() 方法将返回 None
# 如果找到了该模式, search() 方法将返回一个 Match 对象
# Match 对象有一个 group() 方法, 它返回被查找字符串中实际匹配的文本

match = phoneNumRegex.search('My number is 415-555-4343 and 415-123-4343.')
print('Phone number found: ' + match.group())

# 在 Python 中使用正则表达式有几个步骤
# 1．用 import re 导入正则表达式模块
# 2．用 re.compile() 函数创建一个 Regex 对象 (记得使用原始字符串)
# 3．向 Regex 对象的 search() 方法传入想查找的字符串, 它返回一个 Match 对象
# 4．调用 Match 对象的 group() 方法, 返回实际匹配文本的字符串