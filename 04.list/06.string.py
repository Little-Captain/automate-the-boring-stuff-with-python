# 字符串和列表很相似, 可以把字符串看作是单个文本字符的列表
# 对列表的许多操作, 也可以作用于字符串: 按下标取值、切片、
# 用于 for 循环、用于 len(), 以及用于 in 和 not in 操作符

name = 'Zophie'
# 下表取值结果也为 str
print(type(name[0]))
for c in name:
    print(c)

print('Zo' in name)
print('z' in name)

# 可变和不可变数据类型
# 列表是"可变的"数据类型, 它的值可以添加、删除或改变
# 字符串是"不可变的", 它不能被更改
# 尝试对字符串中的一个字符重新赋值, 将导致 TypeError 错误
try:
    name[1] = 'The'
except TypeError:
    print('"str" object dose not support item assignment')
# '改变'一个字符串的正确方式, 是使用切片和连接.
# 从老的字符串那里复制一些部分, 构造一个'新的'字符串, 赋值回去
name = 'Zophie a cat'
name = name[0:7] + 'the' + name[8:12]
print(name)