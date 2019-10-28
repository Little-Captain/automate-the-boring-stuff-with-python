# 在对变量赋值时, 常常会用到变量本身
# 针对 + - * / 和 % 操作符, 都有增强的赋值操作符
spam = 1
print(spam) # 1
spam += 1
print(spam) # 2
spam -= 1
print(spam) # 1
spam *= 2
print(spam) # 2
# / 有理数除法
# // 整数除法
spam //= 2
print(spam) # 1
spam %= 1
print(spam) # 0
print('==========================')
# += 操作符可以完成字符串和列表的连接
# *= 操作符可以完成字符串和列表的复制
spam = 'Hello'
spam += ' world'
print(spam)
bacon = ['zophie']
bacon *= 3
print(bacon)