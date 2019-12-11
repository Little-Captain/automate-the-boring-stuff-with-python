#!/usr/bin/env python

# Python 的 json 模块处理了 JSON 数据字符串和 Python 值之间
# 转换的所有细节，得到了 json.loads() 和 json.dumps() 函数
# JSON 不能存储每一种 Python 值，它只能包含以下数据类型的值：
# 字符串、整型、浮点型、布尔型、列表、字典和 NoneType
# JSON 不能表示 Python 特有的对象

# 用 loads() 函数读取 JSON
# 要将包含 JSON 数据的字符串转换为 Python 的值，就将它传递给 json.loads() 函数
# 基本上，json 是什么类型将会返回什么 Python 类型

import json

# json 字符串必须使用双引号
stringOfJson = '''{
    "name": "Zophie",
    "isCat": true,
    "miceCaught": 0,
    "felineIQ": null
}'''

pythonValue = json.loads(stringOfJson)
print(pythonValue)
print(json.loads('["a", "b"]'))

# 用 dumps 函数写出 JSON
# json.dumps() 函数（它表示“dump string”，而不是“dumps”）
# 将一个 Python 值转换成 JSON 格式的数据字符串
print(json.dumps(pythonValue))
# pythonValue 只能是以下基本 Python 数据类型之一：
# 字典、列表、整型、浮点型、字符串、布尔型或 None
