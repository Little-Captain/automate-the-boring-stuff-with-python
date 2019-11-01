# 双引号
spam = "That is Alice's cat."
print(spam)

print('------------------------')

# 转义字符
spam = 'Say hi to Bob\'s mother.'
print(spam)

print('------------------------')

# 原始字符串
# "原始字符串"完全忽略所有的转义字符, 打印出字符串中所有的倒斜杠
print(r'That is Carol\'s cat.')

print('------------------------')

# 用三重引号的多行字符串
# 在 Python 中, 多行字符串的起止是 3 个单引号或 3 个双引号
# "三重引号"之间的所有引号、制表符或换行, 都被认为是字符串的一部分, 单双引号不需要转义
# Python 的代码块缩进规则不适用于多行字符串 
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# 多行注释
# 虽然井号字符(#)表示这一行是注释, 但多行字符串常常用作多行注释
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

print('------------------------')

def spamx():
    """This is a mutiline comment to help
    explain what the spam() function does."""
    print('Hello!')

spamx()

print('------------------------')

# 字符串下标和切片
# 字符串像列表一样, 使用下标和切片. 可以将字符串'Hello world!'看成是一个列表,
# 字符串中的每个字符都是一个表项，有对应的下标
spam = 'Hello World!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
print(spam[-1:-7:-2])
print(spam)

print('------------------------')

# 字符串的 in 和 not in 操作符
print('Hello' in 'Hello World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello')
print('' in 'spam')
print('cats' in 'cats and dogs')
