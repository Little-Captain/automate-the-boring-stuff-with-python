#!/usr/bin/env python

# 在 Windows 上, 路径书写使用倒斜杠作为文件夹之间的分隔符
# 在 OS X 和 Linux 上, 使用正斜杠作为它们的路径分隔符
# 如果想要程序运行在所有操作系统上, 在编写 Python 脚本时, 就必须处理这两种情况
# 用 os.path.join() 函数来做这件事很简单
import os

print(os.path.join('/usr', 'bin', 'spam'))

names = ['accounts.txt', 'details.csv', 'invite.docx']
for name in names:
    print(os.path.join('~', 'documents', name))

print('---------------------------------')

# 当前工作目录
# 每个运行在计算机上的程序, 都有一个"当前工作目录", 或 cwd(current work directory)
# 所有没有从根文件夹开始的文件名或路径, 都假定在当前工作目录下
# 利用 os.getcwd() 函数, 可以取得当前工作路径的字符串, 并可以利用 os.chdir() 改变它

print('---------------------------------')

old = os.getcwd()
print(old)
os.chdir('/home/lc')
print(os.getcwd())
os.chdir(old)

# 绝对路径与相对路径
# 有两种方法指定一个文件路径:
# 1. "绝对路径", 总是从根文件夹开始(/ or D:\\)
# 2. "相对路径", 它相对于程序的当前工作目录
# 点(.)和点点(..)文件夹
# 它们不是真正的文件夹, 而是可以在路径中使用的特殊名称
# 单个的句点("点")用作文件夹目名称时, 是“这个目录”的缩写
# 两个句点("点点")意思是父文件夹

print('---------------------------------')

os.makedirs('test/test/test', exist_ok=True)

os.system('tree')

print('---------------------------------')

# os.path 模块
# os.path 模块包含了许多与文件名和文件路径相关的有用函数
# 因为 os.path 是 os 模块中的模块, 所以只要执行 import os 就可以导入它

# 处理绝对路径和相对路径
# os.path 模块提供了一些函数, 返回一个相对路径的绝对路径, 以及检查给定的路径是否为绝对路径
# 调用 os.path.abspath(path) 将返回参数的绝对路径的字符串. 这是将相对路径转换为绝对路径的简便方法
# 调用 os.path.isabs(path), 如果参数是一个绝对路径, 就返回 True, 如果参数是一个相对路径, 就返回 False
# 调用 os.path.relpath(path, start) 将返回从 start 路径到 path 的相对路径的字符串. 如果没有提供start, 就使用当前工作目录作为开始路径
print(os.path.abspath('.'))
print(os.path.abspath('/home'))
print(os.path.abspath('/noExist'))
print(os.path.isabs('.'))
print(os.path.isabs('/home'))
print(os.path.isabs('/noExist'))
print(os.path.relpath('.', '/home/lc'))
# 调用 os.path.dirname(path) 将返回一个字符串, 它包含 path 参数中最后一个斜杠之前的所有内容
# 调用 os.path.basename(path) 将返回一个字符串, 它包含path 参数中最后一个斜杠之后的所有内容
print(os.path.dirname('/home/test/ada'))
print(os.path.dirname('/home/test/'))
print(os.path.basename('/home/test/ada'))
print(os.path.basename('/home/test/'))
# 如果同时需要一个路径的目录名称和基本名称, 就可以调用 os.path.split(), 获得这两个字符串的元组
print(os.path.split('/home/test/ada'))
result = (os.path.dirname('/home/test/ada'), os.path.basename('/home/test/ada'))
print(result)
# 通过文件路径, 返回每个文件夹的字符串的列表
# 使用字符串的 split() 方法, 根据 os.path.sep 中的字符串进行分割
# 在 OS X 和Linux 系统上, 返回的列表头上有一个空字符串
path = '/home/test/ada'
print(path.split(os.path.sep))
print('/'.join(path.split(os.path.sep)))

# 查看文件大小和文件夹内容
# os.path 模块提供了一些函数, 用于查看文件的字节数以及给定文件夹中的文件和子文件夹
# 调用 os.path.getsize(path) 将返回 path 参数中`文件`的字节数
# 调用 os.listdir(path) 将返回文件名字符串的列表
# 包含 path 参数中的每个文件(请注意, 这个函数在 os 模块中, 而不是 os.path)
print(os.getcwd())
print(os.path.getsize('./01.file.path.py'))
print(os.listdir('.'))
# 如果想知道这个目录下所有文件的总字节数, 就可以同时使用 os.path.getsize() 和 os.listdir()
totalSize = 0
for filename in os.listdir('.'):
    totalSize += os.path.getsize(os.path.join('.', filename))
print(totalSize)

# 检查路径有效性
# 如果你提供的路径不存在, 许多 Python 函数就会崩溃并报错
# os.path 模块提供了一些函数, 用于检测给定的路径是否存在, 以及它是文件还是文件夹
# 1 如果 path 参数所指的文件或文件夹存在, 调用 os.path.exists(path) 将返回 True, 否则返回 False
# 2 如果 path 参数存在, 并且是一个文件, 调用os.path.isfile(path) 将返回 True, 否则返回False
# 3 如果 path 参数存在, 并且是一个文件夹, 调用 os.path.isdir(path) 将返回 True, 否则返回False
print(os.path.exists('.'))
print(os.path.exists('./test/'))
print(os.path.exists('./test/123'))
print(os.path.isdir('01.file.path.py'))
print(os.path.isfile('01.file.path.py'))
