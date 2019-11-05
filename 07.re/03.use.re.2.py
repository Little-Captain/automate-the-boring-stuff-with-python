#!/usr/bin/env python

import re

## 利用括号分组
# 添加括号将在正则表达式中创建"分组"
# group(gIndex)
# gIndex 不传, 或传入 0: 匹配的整个文本
# gIndex n: 匹配的第 n 组
# phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')

print('-----------------------------------')

# match = phoneNumRegex.search('My number is 415-555-4343 and 415-123-4343.')
match = phoneNumRegex.search('My number is 415-555-4343 and (415) 123-4343.')
print('Phone number found: ' + match.group())
print('Phone number found 1: ' + match.group(1))
print('Phone number found 2: ' + match.group(2))

print('-----------------------------------')

# 返回元组
results = match.groups()
areaCode, mainNumber = match.groups()
print(results)
print(areaCode, mainNumber)

print('-----------------------------------')

# 用管道匹配多个分组
# 字符 | 称为"管道". 希望匹配许多表达式中的一个时, 就可以使用它
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

print('-----------------------------------')

# 利用 findall() 方法, 可以找到"所有"匹配的地方
# 可以使用管道来匹配多个模式中的一个, 作为正则表达式的一部分
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
# 如果需要匹配真正的管道字符, 就用倒斜杠转义, 即 \|

# 用问号实现可选匹配
# 字符 ? 表明它前面的分组在这个模式中是可选的

print('-----------------------------------')

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# 如果需要匹配真正的问号字符, 就使用转义字符 \?

print('-----------------------------------')

# 用星号匹配零次或多次
# * 意味着"匹配零次或多次", 即星号之前的分组, 可以在文本中出现任意次
# 它可以完全不存在, 或一次又一次地重复
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo2.group())
# 如果需要匹配真正的星号字符, 就在正则表达式的星号字符前加上倒斜杠, 即 \*

print('-----------------------------------')

# 用加号匹配一次或多次
# * 意味着"匹配零次或多次", + 则意味着"匹配一次或多次"
# 星号不要求前面的分组出现在匹配的字符串中, 
# 加号要求前面的分组必须"至少出现一次"
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
if mo1:
    print(mo1.group())
else:
    print(mo1)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
# 如果需要匹配真正的加号字符, 在加号前面加上倒斜杠实现转义: \+

print('-----------------------------------')

# 用花括号匹配特定次数
# 如果想要一个分组重复特定次数, 就在正则表达式中该分组的后面, 跟上花括号包围的数字
# 除了一个数字, 还可以指定一个范围, 即在花括号中写下一个最小值、一个逗号和一个最大值
# 也可以不写花括号中的第一个或第二个数字, 不限定最小值或最大值
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
print(mo1.groups())
mo2 = haRegex.search('Ha')
print(mo2 == None)