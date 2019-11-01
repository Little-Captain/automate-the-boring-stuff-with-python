#!/usr/bin/env python
# 有用的字符串方法

# 字符串方法 upper()、lower()、isupper() 和 islower()
# upper() 和 lower() 字符串方法返回一个新字符串, 其中原字符串的
# 所有字母都被相应地转换为大写或小写. 字符串中非字母字符保持不变
spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

print('-----------------------')

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

print('-----------------------')

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())
print(spam.upper().isupper())
print(spam.lower().islower())

print('-----------------------')

# isX 字符串方法:这些方法返回一个布尔值, 描述了字符串的特点
# isalpha() 返回 True, 如果字符串只包含字母, 并且非空
# isalnum() 返回 True, 如果字符串只包含字母和数字, 并且非空
# isdecimal() 返回 True, 如果字符串只包含数字字符, 并且非空
# isspace() 返回 True, 如果字符串只包含空格、制表符和换行, 并且非空
# istitle() 返回 True, 如果字符串仅包含以大写字母开头、后面都是小写字母的单词
print('hello'.isalpha())
print('hello1231'.isalpha())
print('hello1231'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print(''.isspace())
print(' '.isspace())
print('This Is Title Case.'.istitle())
print('This Is Title Case 123.'.istitle())
print('This Is not Title Case.'.istitle())
print('This Is NOT Title Case Either.'.istitle())

print('-----------------------')

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

print('-----------------------')

# 字符串方法 startswith() 和 endswith()
# startswith() 和 endswith() 方法返回 True,
# 如果它们所调用的字符串以该方法传入的字符串开始或结束
# 否则, 方法返回 False
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))
print('Hello world!'.endswith('Hello world!'))
# 如果只需要检查字符串的开始或结束部分是否等于另一个字符串, 而不是整个字符串,
# 这些方法就可以替代等于操作符 ==, 这很有用
print('abc' == 'abc')

print('-----------------------')

# 字符串方法 join() 和 split()
# 如果有一个字符串列表, 需要将它们连接起来, 成为一个单独的字符串,
# join() 方法就很有用. join() 方法在一个字符串上调用, 参数是一个字符串列表,
# 返回一个字符串. 返回的字符串由传入的列表中每个字符串连接而成 
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

print('-----------------------')

# split() 方法做的事情正好相反:它针对一个字符串调用, 返回一个字符串列表
# 默认情况下, split 使用各种空白字符分割字符串, 诸如空格、制表符或换行符
# 这些空白字符不包含在返回列表的字符串中
# 也可以向 split() 方法传入一个分割字符串, 指定它按照不同的字符串分割
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

print('-----------------------')

# 一个常见的 split() 用法, 是按照换行符分割多行字符串
# 向 split() 方法传入参数 '\n', 我们按照换行符分割变量中存储的多行字符串
# 返回列表中的每个表项, 对应于字符串中的一行
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

print('-----------------------')

# 用 rjust()、ljust() 和 center() 方法对齐文本
# 利用 rjust()、ljust() 和 center() 让你确保字符串整齐对齐, 即使你不清楚字符串有多少字符
# rjust() 和 ljust() 字符串方法返回调用它们的字符串的填充版本, 通过插入空格来对齐文本
# 第一个参数:一个整数长度, 用于对齐字符串
# 第二个参数:可选, 指定一个填充字段, 取代空格字符
print('%r' % 'Hello'.rjust(10))
print('%r' % 'Hello'.rjust(20))
print('%r' % 'Hello World'.rjust(20))
print('%r' % 'Hello'.ljust(10))
print('%r' % 'Hello'.ljust(10, '*'))

print('-----------------------')

# center() 字符串方法与 ljust() 与 rjust() 类似, 但它让文本居中, 而不是左对齐或右对齐
print('%r' % 'Hello'.center(11))
print('%r' % 'Hello'.center(10, '*'))

print('-----------------------')
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

print('-----------------------')

# 用 strip()、rstrip() 和 lstrip() 删除空白字符
# strip() 字符串方法将返回一个新的字符串, 它的开头或末尾都没有空白字符
# lstrip() 和 rstrip() 方法将相应删除左边或右边的空白字符
spam = ' Hello World   \n'
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
# 有一个可选的字符串参数，指定两边的哪些字符应该删除
# 字符串参数中包含的字符都会被删除
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
print(spam.lstrip('ampS'))
print(spam.rstrip('ampS'))

print('-----------------------')

# 用 pyperclip 模块拷贝粘贴字符串
# pyperclip 模块有 copy() 和 paste() 函数,
# 可以向计算机的剪贴板发送文本, 或从它接收文本
# 将程序的输出发送到剪贴板, 使它很容易粘贴到邮件、文字处理程序或其他软件中
import pyperclip

pyperclip.copy('Hello world!')
print(pyperclip.paste())