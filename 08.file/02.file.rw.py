#!/usr/bin/env python

# 纯文本文件: 只包含基本文本字符, 不包含字体、大小和颜色信息
# 二进制文件: 所有其他文件类型, 诸如字处理文档、PDF、图像、电子表格和可执行程序

# 读写文件有 3 个步骤:
# 1. 调用 open() 函数, 返回一个 File 对象
# 2. 调用 File 对象的 read() 或 write() 方法
# 3. 调用 File 对象的 close() 方法, 关闭该文件
helloFile = open('hello.txt') # 默认是`只读`模式 'r'
# 读取文件内容
# File.read 将整个文件的内容读取为一个字符串值
whole = helloFile.read()
print(whole)
print(whole.split('\n'))
helloFile.seek(0) # 文件指针定位到开始位置
# File.readlines() 从该文件取得一个字符串的列表, 列表中的每个字符串就是文本中的每一行
# 请注意, 每个字符串值都以一个换行字符 \n 结束
print(helloFile.readlines())
helloFile.close()

print('---------------------------')

# 写入文件
# Python 允许你将内容写入文件, 方式与 print() 函数将字符串"写"到屏幕上类似
# 如果打开文件时用读模式, 就不能写入文件.
# 需要以"写入纯文本模式"或"添加纯文本模式"打开该文件, 简称为"写模式"和"添加模式"
# 写模式: 将覆写原有的文件. 将'w'作为第二个参数传递给open(), 以写模式打开该文件
# 添加模式: 将在已有文件的末尾添加文本. 将'a'作为第二个参数传递给open(), 以添加模式打开该文件
# 如果传递给 open() 的文件名不存在, 写模式和添加模式都会创建一个新的空文件
# 在读取或写入文件后, 调用 close() 方法, 然后才能再次打开该文件
baconFile = open('bacon.txt', 'w')
# write 返回写入的字符个数, 包括换行符
# 请注意, write() 不会在字符串的末尾自动添加换行字符. 必须自己添加该字符.
print(baconFile.write('Hello bacon!\n'))
baconFile.close()
baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
# r: 只读模式, 默认
# w: 写入模式
# a: 添加模式