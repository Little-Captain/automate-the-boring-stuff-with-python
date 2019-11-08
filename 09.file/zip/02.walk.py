#!/usr/bin/env python

# 遍历目录树

import os

for folderName, subfolders, filenames in os.walk('/mnt/d/Book/Python'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print()

# os.walk() 函数被传入一个字符串值，即一个文件夹的路径。你可以在一个 for 循环语句中
# 使用 os.walk() 函数，遍历目录树，就像使用 range() 函数遍历一个范围的数字一样。
# 不像 range()，os.walk() 在循环的每次迭代中，返回 3 个值：
# 1．当前文件夹名称的字符串。
# 2．当前文件夹中子文件夹的字符串的列表。
# 3．当前文件夹中文件的字符串的列表。

# 所谓当前文件夹，是指 for 循环当前迭代的文件夹。程序的当前工作目录，不会因为 os.walk() 而改变。