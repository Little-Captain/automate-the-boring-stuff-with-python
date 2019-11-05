#!/usr/bin/env python

import re
import pprint

# 通配字符
# 在正则表达式中, .(句点)字符称为"通配符". 它匹配除了换行之外的所有字符
# 要匹配真正的句点, 就是用倒斜杠转义: \.
atRegex = re.compile(r'.at')
result = atRegex.findall('The cat in the hat sat on the flat mat.')
pprint.pprint(result)

print('--------------------------------')

# 用点-星匹配所有字符: .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

print('--------------------------------')

# 点-星使用"贪心"模式: 它总是匹配尽可能多的文本
# 要用"非贪心"模式匹配所有文本, 就使用点-星和问号: .*?
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

print('--------------------------------')

# 用句点字符匹配换行
# 点-星将匹配除换行外的所有字符. 通过传入 re.DOTALL 作为 re.compile() 的第二个参数,
# 可以让句点字符匹配所有字符，包括换行字符
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

# ? 匹配零次或一次前面的分组
# * 匹配零次或多次前面的分组
# + 匹配一次或多次前面的分组
# {n} 匹配 n 次前面的分组
# {n,} 匹配 n 次或更多前面的分组
# {,m} 匹配零次到 m 次前面的分组
# {n,m} 匹配至少 n 次、至多 m 次前面的分组
# {n,m}? 或 *? 或 +? 对前面的分组进行非贪心匹配
# ^spam 意味着字符串必须以 spam 开始
# spam$ 意味着字符串必须以 spam 结束
# . 匹配所有字符, 换行符除外
# \d、\w 和 \s 分别匹配数字、单词和空格
# \D、\W 和 \S 分别匹配出数字、单词和空格外的所有字符
# [abc] 匹配方括号内的任意字符(诸如 a、b 或 c)
# [^abc]匹 配不在方括号内的任意字符