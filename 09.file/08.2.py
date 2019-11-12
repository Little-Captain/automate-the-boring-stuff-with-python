#!/usr/bin/env python

# 编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，
# 比方说，超过 100MB 的文件（回忆一下，要获得文件的大小，
# 可以使用 os 模块的 os.path.getsize()）
# 将这些文件的绝对路径打印到屏幕上

import os


def printBigFile(path):
    '''
    打印大文件的路径及其大小
    '''
    for folder, _, filenames in os.walk(path):
        for filename in filenames:
            fullFileName = os.path.join(folder, filename)
            size = os.path.getsize(fullFileName) >> 20
            if size >= 100:
                print('%s: %d MB' % (fullFileName, size))


printBigFile('/mnt/d/Book')
