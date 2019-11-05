#!/usr/bin/env python

import re
import pprint

# \d: 0 到 9 的任何数字
# \D: 除 0 到 9 的数字以外的任何字符
# \w: 任何字母、数字或下划线字符(可以认为是匹配"单词"字符)
# \W: 除字母、数字和下划线以外的任何字符
# \s: 空格、制表符或换行符(可以认为是匹配"空白"字符)
# \S: 除空格、制表符和换行符以外的任何字符

# 字符分类对于缩短正则表达式很有用
xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.findall('12 drumers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens 2 doves, 1 partridge')
pprint.pprint(result)

print('----------------------------')

# 建立自己的字符分类
# 用方括号定义自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
result = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
pprint.pprint(result)

print('----------------------------')

# 可以使用短横表示字母或数字的范围
# 在方括号内, 普通的正则表达式符号不会被解释(不需要加上倒斜杠转义.、*、?或()字符)
# 通过在字符分类的左方括号后加上一个插入字符(^), 就可以得到"非字符类"
# 非字符类将匹配不在这个字符类中的所有字符
consonantRegex = re.compile(r'[^aeiouAEIOU]')
result = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
pprint.pprint(result)

print('----------------------------')

# 插入字符和美元字符
# 可以在正则表达式的开始处使用插入符号(^), 表明匹配必须发生在被查找文本开始处
# 类似地, 可以在正则表达式的末尾加上美元符号($), 表示该字符串必须以这个正则表达式的模式结束
# 可以同时使用 ^ 和 $, 表明整个字符串必须匹配该模式,
# 也就是说, 只匹配该字符串的某个子集是不够的
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo.group())
mo = beginsWithHello.search('He said Hello.')
print('mo == none %s' % str(mo == None))

print('----------------------------')

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo.group())
mo = endsWithNumber.search('Your number is four two')
print('mo == none %s' % str(mo == None))

print('----------------------------')

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo.group())
mo = wholeStringIsNum.search('1231 131235123')
print('mo == none %s' % str(mo == None))
# 如果使用了 ^ 和 $, 那么整个字符串必须匹配该正则表达式
