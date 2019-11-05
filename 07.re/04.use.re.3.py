#!/usr/bin/env python

import re
# 贪心和非贪心匹配
# Python 的正则表达式默认是"贪心"的
# 在有二义的情况下, 它们会尽可能匹配最长的字符串
# 花括号的"非贪心"版本匹配尽可能最短的字符串, 即在结束的花括号后跟着一个问号
# 贪心
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
# 非贪心
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
# 问号在正则表达式中可能有两种含义:
# 1. 声明非贪心匹配
# 2. 表示可选的分组

print('---------------------------------------')

# findall() 方法
# search() 将返回一个 Match 对象, 包含被查找字符串中的"第一次"匹配的文本
# findall() 将返回一个列表, 包含被查找字符串中的所有匹配
# 1. 在正则表达式中没有分组: 列表中的每个字符串都是一段被查找的文本, 它匹配该正则表达式
# 2. 在正则表达式中有分组: 将返回元组的列表. 每个元组表示一个找到的匹配,
#    其中的项就是正则表达式中每个分组的匹配字符串
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)
# findall() 方法的返回结果的总结:
# 1．如果调用在一个没有分组的正则表达式上, 方法将返回一个匹配字符串的列表
# 2．如果调用在一个有分组的正则表达式上, 方法将返回一个字符串的元组的列表(每个分组对应一个字符串)