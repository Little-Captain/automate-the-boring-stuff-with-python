#!/usr/bin/env python

# shutil(shell util) 模块主要用于
# 复制、移动、改名和删除文件

# 复制文件和文件夹
# 调用 shutil.copy(source, destination)
# 将路径 source 处的文件复制到路径 destination 处的文件夹
# 如果 destination 是一个文件名, 它将作为被复制文件的新名字
# 该函数返回一个字符串，表示被复制文件的路径。
import shutil

shutil.copy('./spam.txt', '/mnt/d/Downloads/spam_copy.txt')
shutil.copy('eggs.txt', '/mnt/d/Downloads/eggs_copy.txt')

# shutil.copy() 将复制一个文件，shutil.copytree() 将复制整个文件夹，以及它包含的文件夹和文件
# 调用 shutil.copytree(source, destination)，将路径 source 处的文件夹，包括它的所有文件和
# 子文件夹，复制到路径 destination 处的文件夹。source 和 destination 参数都是字符串
# 该函数返回一个字符串，是新复制的文件夹的路径。
# print(shutil.copytree('test', '/mnt/d/Downloads/test_copy'))

print('---------------------------------')

# 文件和文件夹的移动与改名
# 调用 shutil.move(source, destination)，将路径 source 处的文件夹移动到路径 destination，
# 并返回新位置的绝对路径的字符串
# 如果 destination 指向一个文件夹，source 文件将移动到 destination 中，并保持原来的文件名
# 1. 如果文件夹已存在，就是将文件移入
# 2. 如果文件夹内已存在同名文件，就会覆写文件
# 因为用这种方式很容易不小心覆写文件，所以在使用 move() 时应该注意。
# source destination 路径可以指定文件名
# print(shutil.move('test', '/mnt/d/Downloads'))
# print(shutil.move('eggs_copy.txt', '/mnt/d/Downloads/eggs2.txt'))
# 构成目的地的文件夹必须已经存在，否则 Python 会抛出异常

print('---------------------------------')

# 永久删除文件和文件夹
# 利用 os 模块中的函数，可以删除一个文件或一个空文件夹。
# 利用 shutil 模块，可以删除一个文件夹及其所有的内容。
# 用 os.unlink(path) 将删除 path 处的文件。
# 调用 os.rmdir(path) 将删除 path 处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹。
# 调用 shutil.rmtree(path) 将删除 path 处的文件夹，它包含的所有文件和文件夹都会被删除。

# 在程序中使用这些函数时要小心！可以第一次运行程序时，注释掉这些调用，并且加上print()调用，
# 显示会被删除的文件。这样做是一个好主意。
import os

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

# 用 send2trash 模块安全地删除
# 因为 Python 内建的 shutil.rmtree() 函数不可恢复地删除文件和文件夹，所以用起来可能有危险
# 删除文件和文件夹的更好方法，是使用第三方的 send2trash 模块
# 利用 send2trash，比 Python 常规的删除函数要安全得多，因为它会将文件夹和文件发送到计算机的垃圾箱或回收站，而不是永久删除它们。
import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

# 一般来说，总是应该使用 send2trash.send2trash() 函数来删除文件和文件夹。
# 虽然它将文件发送到垃圾箱，让你稍后能够恢复它们，但是这不像永久删除文件，
# 不会释放磁盘空间。如果你希望程序释放磁盘空间，就要用 os 和 shutil 来删除文件和文件夹。
# 请注意，send2trash() 函数只能将文件送到垃圾箱，不能从中恢复文件。