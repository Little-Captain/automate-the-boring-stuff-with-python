#!/usr/bin/env python

# 利用 shelve 模块, 可以将 Python 程序中的变量保存到二进制的 shelf 文件中
# 这样程序就可以从硬盘中恢复变量的数据
# shelve 模块让你在程序中添加"保存"和"打开"功能
# 要保存 Python 程序中的数据，那就应该使用 shelve 模块

import shelve

shelfFile = shelve.open('mydata')
print(type(shelfFile))
cats = ['zophie', 'pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()

print('---------------------------')

# shelf 值不必用读模式或写模式打开，因为它们在打开后，既能读又能写
shelfFile = shelve.open('mydata')
print(type(shelfFile))
c = shelfFile['cats']
print(c)
print(type(c))
shelfFile.close()

print('---------------------------')

# 就像字典一样，shelf 值有 keys() 和 values() 方法，返回 shelf 中键和值的类似列表的值
# 因为这些方法返回类似列表的值，而不是真正的列表，所以应该将它们传递给 list() 函数，取得列表的形式
shelfFile = shelve.open('mydata')
keys = shelfFile.keys()
print(type(keys))
print(keys)
print(list(keys))
values = shelfFile.values()
print(type(values))
print(keys)
print(list(values))
shelfFile.close()
