#!/usr/bin/env python

import re
import pyperclip

# 1. 从剪贴板取得文本
# 2. 找出文本中所有的电话号码和 E-mail 地址
# 3. 将它们粘贴到剪贴板
# 现在你可以开始思考, 如何用代码来完成工作. 代码需要做下面的事情:
# 1. 使用 pyperclip 模块复制和粘贴字符串。
# 2. 创建两个正则表达式, 一个匹配电话号码, 另一个匹配 E-mail 地址
# 3. 对两个正则表达式, 找到所有的匹配, 而不只是第一次匹配
# 4. 将匹配的字符串整理好格式, 放在一个字符串中, 用于粘贴
# 5. 如果文本中没有找到匹配, 显示某种消息

# 为电话号码创建一个正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             # area code
    (\s|-|\.)?                     # separator
    (\d{3})                        # first 3 digits
    (\s|-|\.)                      # separator
    (\d{4})                        # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

# 为E-mail 地址创建一个正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+         # username
    @                         # symbol
    [a-zA-Z0-9.-]+            # domain name
    (\.[a-zA-Z]{2,4})         # top domain name
    )''', re.VERBOSE)

# 在剪贴板文本中找到所有匹配
text = pyperclip.paste()
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

# 所有匹配连接成一个字符串, 复制到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# search() 查找单次匹配
# findall() 查找所有匹配
# sub() 对文本进行查找和替换