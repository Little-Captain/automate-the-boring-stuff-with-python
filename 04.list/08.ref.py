# 值
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

print('------------------------')

# 引用
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
# spam cheese 的值相同, 都是同一个引用
cheese[1] = 'Hello!'
print(spam)
print(cheese)

# 当创建列表时, 将对列表的引用赋给了变量
# 变量包含对列表值的引用, 而不是列表值本身
# 对于字符串和整数值, 变量就包含了字符串或整数值
# 在变量必须保存`可变数据类型`的值时, 例如列表或字典, Python 就使用引用
# 对于`不可变数据类型`的值, 例如字符串、整型或元组, Python 变量就保存值本身
# 虽然 Python 变量在技术上包含了对列表或字典值的引用, 但人们通常随意地说, 该变量包含了列表或字典
# 总结
# 引用: 可变数据类型
# 值: 不可变数据类型
# 以上解释的正确性有待商榷

print('------------------------')

def eggs(parameter):
    parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# copy 模块的 copy() 和 deepcopy() 函数
# 在处理列表和字典时, 尽管传递引用常常是最方便的方法, 但如果函数修改了
# 传入的列表或字典, 你可能不希望这些变动影响原来的列表或字典. 要做到这一点，
# Python 提供了名为 copy 的模块，其中包含 copy() 和 deepcopy() 函数
# 第一个函数 copy.copy(), 可以用来复制列表或字典这样的可变值, 而不只是复制引用

print('------------------------')

import copy
spam = ['a', 'b', 'c']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# 如果要复制的列表中包含了列表, 那就使用 copy.deepcopy() 函数来代替
# deepcopy() 函数将同时复制它们内部的列表