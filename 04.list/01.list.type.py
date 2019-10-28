print([1, 2, 3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['hello', 3.14159, True, None, 42])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

print('===============================')

# 用下标取得列表中的单个值
print(spam[0])
print(spam[3])

try:
    print(spam[4])
except IndexError:
    print('list index out of range')

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(spam[0])
print(spam[0][1])
print(spam[1][4])

print('===============================')

# 负数下标
# -n 倒数第 n 个
print(spam[1][-1])

print('===============================')

# 利用切片取得子列表
# 下标可以从列表中取得单个值, "切片"可以从列表中取得多个值, 结果是一个新列表
# list[start:end:step]
# start: 开始(包含)
# end: 结束(不包含)
# step: 步长
print(spam[1][0:5:2])

print('===============================')

# 用len()取得列表的长度
print(len(spam))

print('===============================')

# 用下标改变列表中的值
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)

# 列表连接和列表复制
# + 操作符可以连接两个列表, 得到一个新列表, 就像它将两个字符串合并成一个新字符串一样
# * 操作符可以用于一个列表和一个整数, 实现列表的复制

print('===============================')

print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)

# 用 del 语句从列表中删除值
# del 语句将删除列表中下标处的值, 表中被删除值后面的所有值, 都将向前移动一个下标

print('===============================')

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

# del 语句也可用于一个简单变量, 删除它, 作用就像是"取消赋值"语句
# 在实践中, 几乎永远不需要删除简单变量. del 语句几乎总是用于删除列表中的值

print('===============================')

spam = 1
print(spam)
del spam
try:
    print(spam)
except NameError:
    print("name 'spam' is not defined")