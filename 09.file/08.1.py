#!/usr/bin/env python

# 编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）
# 不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中

import os
import shutil


def deal(path, type):
    """
    path: 需要遍历的目录
    type: 要复制的文件类型
    结果将被拷贝到 /mnt/d/Downloads/{type} 这个文件夹中
    """
    path = os.path.abspath(path)
    if not os.path.exists(path):
        return
    destinationPath = os.path.join('/mnt/d/Downloads', type)
    os.makedirs(destinationPath, exist_ok=True)
    # 使用 walk 递归遍历 path
    for folder, _, filenames in os.walk(path):
        files = list(map(
            lambda x: os.path.join(folder, x),
            list(filter(lambda x: x.endswith('.%s' % type), filenames))
        ))
        # 拷贝 type 类型的文件到 /mnt/d/Downloads/{type} 文件夹
        for file in files:
            shutil.copy(file, destinationPath)


deal('/mnt/d/Book/Linux', 'txt')
