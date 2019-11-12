#!/usr/bin/env python

import os
import re
import shutil

# 编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，
# 诸如spam001.txt, spam002.txt 等，并定位缺失的编号
# （例如存在spam001.txt 和spam003.txt，但不存在spam002.txt）
# 让该程序对所有后面的文件改名，消除缺失的编号。


def findMissCode(path, prefix, codeLength=3):
    path = os.path.abspath(path)
    for folder, _, filenames in os.walk(path):
        regex = re.compile(r'%s(\d{%d})(\..*)' % (prefix, codeLength))

        dict = {}
        for name in filenames:
            m = regex.search(name)
            if m != None:
                dict[int(m.group(1))] = (m.group(), m.group(2))
        oldOrders = list(dict.keys())
        oldOrders.sort()
        for i in range(len(oldOrders)):
            oldname = os.path.join(path, dict[oldOrders[i]][0])
            newname = os.path.join(
                path,
                '%s%s%s' % (prefix,
                            str(oldOrders[0] + i).rjust(codeLength, '0'),
                            dict[oldOrders[i]][1])
            )
            shutil.move(oldname, newname)


# findMissCode('/mnt/d/Downloads/test', 'spam')

# 作为附加的挑战，编写另一个程序，在一些连续编号的文件中，
# 空出一些编号， 以便加入新的文件

def freeUpCode(path, prefix, freeUpIndex, codeLength=3):
    path = os.path.abspath(path)
    for folder, _, filenames in os.walk(path):
        regex = re.compile(r'%s(\d{%d})(\..*)' % (prefix, codeLength))

        dict = {}
        for name in filenames:
            m = regex.search(name)
            if m != None:
                dict[int(m.group(1))] = (m.group(), m.group(2))
        oldOrders = list(dict.keys())
        oldOrders.sort()
        for i in range(len(oldOrders)):
            oldname = os.path.join(path, dict[oldOrders[i]][0])
            if i < freeUpIndex:
                newname = os.path.join(
                    path,
                    '%s%s%s' % (prefix,
                                str(oldOrders[0] + i).rjust(codeLength, '0'),
                                dict[oldOrders[i]][1])
                )
            else:
                newname = os.path.join(
                    path,
                    '%s%s%s' % (prefix,
                                str(oldOrders[0] + i + 1).rjust(codeLength, '0'),
                                dict[oldOrders[i]][1])
                )
            shutil.move(oldname, newname)
freeUpCode('/mnt/d/Downloads/test', 'spam', 3)