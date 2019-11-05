#!/usr/bin/env python

import re
import pprint

# 不区分大小写的匹配
# 通常, 正则表达式用你指定的大小写匹配文本
# 要让正则表达式不区分大小写,
# 可以向 re.compile() 传入 re.IGNORECASE 或 re.I, 作为第二个参数
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
print(mo.group())
mo = robocop.search('rOBOcOP is part man, part machine, all cop.')
print(mo.group())
mo = robocop.search(
    'Al, why dose your programing book talk about robocop so much ?')
print(mo.group())

print('--------------------------------')

# 用 sub() 方法替换字符串
# 正则表达式不仅能找到文本模式, 而且能够用新的文本替换掉这些模式
# Regex 对象的 sub() 方法需要传入两个参数:
# 第一个参数: 一个字符串, 用于替换匹配到的字符串
# 第二个参数: 一个字符串, 需要替换处理的原始字符串
# sub() 方法返回替换完成后的字符串
namesRegex = re.compile(r'Agent \w+')
result = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret doocuments to Agent Bob.')
print(result)
# 使用匹配的文本本身，作为替换的一部分
# 在 sub() 的第一个参数中, 可以输入 \1、\2、\3…… 表示"在替换中输入分组1、2、3……的文本"
agentNamesRegex = re.compile(r'Agent (\w)\w*')
result = agentNamesRegex.sub(
    r'\1******', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(result)

print('--------------------------------')

# 管理复杂的正则表达式
# 匹配复杂的文本模式, 可能需要长的、费解的正则表达式,
# 这时我们需要分解和解释说明这个正则表达式
# 可以告诉 re.compile(), 忽略正则表达式字符串中的空白符和注释, 从而做到这一点
# 要实现这种详细模式, 可以向 re.compile() 传入变量 re.VERBOSE, 作为第二个参数
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code
    (\s|-|\.)?                   # separator
    \d{3}                        # first 3 digits
    (\s|-|\.)                    # separator
    \d{4}                        # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)
# 正则表达式字符串中的注释规则, 与普通的 Python 代码一样:
# # 符号和它后面直到行末的内容都被忽略.
# 表示正则表达式的多行字符串中, 多余的空白字符也不认为是要匹配的文本模式的一部分
mo = phoneRegex.search('(131) 312-5234 ext 4213 sdfasgwerasdfsad')
print(mo.group())

# 组合使用 re.IGNORECASE、re.DOTALL 和 re.VERBOSE
# 可以使用管道字符(|)将值组合起来. 管道字符在这里称为"按位或"操作符
someRegex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


