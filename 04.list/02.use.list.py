# 使用列表
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print(' ' + name)

print('------------------------------')

# 列表用于循环
# range(4) : range(0, 4).
# range(start, end, step) start 包含, end 不包含
for i in range(4):
    print(i)

print('------------------------------')

for i in [1, 2, 3, 4]:
    print(i)

print('------------------------------')

for i in range(len(catNames)):
    print('Index ' + str(i) + ' in cat names is: ' + catNames[i])

print('------------------------------')

# in 和 not in 操作符
# 利用 in 和 not in 操作符，可以确定一个值否在列表中
if 'howdy' not in ['hello', 'hi', 'howdy', 'heyas']:
    print('howdy not in')
else:
    print('howdy in')

print('------------------------------')

pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

print('------------------------------')

# 多重赋值技巧
# 多重赋值技巧是一种快捷方式, 让你在一行代码中, 用列表中的值为多个变量赋值
# 变量的数目和列表的长度必须严格相等, 否则 Python 将给出 ValueError
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size, color, disposition)

s, c, d = cat
print(s, c, d)