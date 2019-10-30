# 字典的索引可以使用许多不同数据类型, 不只是整数
# 字典的索引被称为“键”, 键及其关联的值称为“键-值”对
myCat = {'size': 'fat', 1: 2}
print(myCat['size'])
print(myCat[1])

print('---------------------------')

# 字典中的表项是不排序的
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
# 相等比较时: 列表中的值顺序重要
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# 相等比较时: 字典中的键-值对顺序不重要
print(eggs == ham)
# 尝试访问字典中不存在的键, 将导致 KeyError 出错信息
try:
    print(eggs['nam'])
except KeyError:
    print('KeyError')

print('---------------------------')

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
while False:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

print('---------------------------')

# keys(): 键      type: dict_keys
# values(): 值    type: dict_values
# items(): 键-值对 type: dict_items
# 这些方法返回的值不是真正的列表, 它们不能被修改, 没有 append() 方法
for k in birthdays.keys():
    print(k)
for v in birthdays.values():
    print(v)
for item in birthdays.items():
    print(item)
for (k, v) in birthdays.items():
    print(k, v)
# 转换为列表
print(list(birthdays.keys()))
print(list(birthdays.values()))
print(list(birthdays.items()))

print('---------------------------')

# 检查字典中是否存在键或值
# in 和 not in 操作符可以检查值是否存在于列表中
# 也可以利用这些操作符, 检查某个键或值是否存在于字典中
print('Alice' in birthdays.keys())
# 直接在 dict 上使用 in, 就是看 keys 是否包含该键
# 如果想要检查一个值是否为字典中的键, 就可以用关键字 in (或 not in), 作用于该字典本身
print('Alice' in birthdays)
print('Alie' in birthdays)

print('---------------------------')

# get() 方法
# get() 方法, 它有两个参数: 要取得其值的键, 以及如果该键不存在时, 返回的备用值
print(birthdays.get('aaa'))
print(birthdays.get('Alice', 'I don\'t know'))
try:
    print(birthdays['aaa'])
except KeyError:
    print('KeyError')

print('---------------------------')

# setdefault() 方法
# 为字典中某个键设置一个默认值, 当该键没有任何值时使用它
# setdefault(): 传递给该方法的第一个参数是要检查的键; 第二个参数是如果该键不存在时要设置的值
# 如果该键确实存在, 方法就会返回键的值
# setdefault(key, defaultValue):
# 1. key 不存在, 设置 key 的值为 defaultValue, 并返回该默认值
# 2. key 存在, 不重新设置 key 的值, 返回 key 的值
print(birthdays.setdefault('Alice', 'July 29'))
print(birthdays.setdefault('aaa', 'July 22'))
print(birthdays.setdefault('aaa', 'July 23'))

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    # count[character] = count[character] + 1
    count[character] += 1
print(count)