# 元组数据类型, 它是列表数据类型的不可变形式
eggs = ('hello', 42, 0.5)
print(eggs)
print(eggs[1])
# 元组像字符串一样, 是不可变的. 元组不能让它们的值被修改、添加或删除
try:
    eggs[1] = 1
except TypeError:
    print('"tuple" object dose not support item assignment')

eggs = (1)
print(eggs)
eggs = (1,)
print(eggs)

# 用 list() 和 tuple() 函数来转换类型
# 函数 list() 和 tuple() 将返回传递给它们的值的列表和元组版本
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
print(tuple('hello'))