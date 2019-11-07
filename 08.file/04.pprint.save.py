#!/usr/bin/env python

# 用pprint.pformat()函数保存变量

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]

# print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# import 语句导入的模块本身就是 Python 脚本
# 如果来自 pprint.pformat() 的字符串保存为一个 .py 文件，该文件就是一个可以导入的模块，像其他模块一样
# 由于 Python 脚本本身也是带有 .py 文件扩展名的文本文件，
# 所以你的 Python 程序甚至可以生成其他 Python 程序。然后可以将这些文件导入到脚本中。
import myCats

cs = myCats.cats

print(cs[0])
print(cs[0]['name'])

# 创建一个 .py 文件（而不是利用 shelve 模块保存变量）的好处在于，
# 因为它是一个文本文件，所以任何人都可以用一个简单的文本编辑器读取和修改该文件的内容。
# 但是，对于大多数应用，利用 shelve 模块来保存数据，是将变量保存到文件的最佳方式。
# 只有基本数据类型，诸如整型、浮点型、字符串、列表和字典，可以作为简单文本写入一个文件。