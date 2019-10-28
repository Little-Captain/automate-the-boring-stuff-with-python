# 方法和函数是一回事, 只是它是调用在一个值上

# 用 index() 方法在列表中查找值
# 返回下表. 如果值不在列表中, Python 就报 ValueError
# 如果列表中存在重复的值, 就返回它第一次出现的下标
spam = ['hello', 'hi', 'hi', 'howdy', 'heyas']
print(spam.index('hi'))

print('--------------------------------')

# 用 append() 和 insert() 方法在`原列表`中添加值
# append() 和 insert() 返回的都是 None
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
spam.insert(1, 'panda')
print(spam)

print('--------------------------------')

# 用 remove() 方法从列表中删除值
# 给 remove() 方法传入一个值, 它将从被调用的列表中删除
# 试图删除列表中不存在的值, 将导致 ValueError 错误
# 如果该值在列表中出现多次, 只有第一次出现的值会被删除
# 如果知道想要删除的值在列表中的下标, 使用 del 语句即可
spam =['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
del spam[0]
print(spam)

print('--------------------------------')

# 用 sort() 方法将列表中的值排序
# 数值的列表或字符串的列表, 能用 sort() 方法排序
# sort() 返回值为 None
spam = [1, 2, 5, 3, 2, 14, 9, -7]
spam.sort()
print(spam)
spam.sort(reverse = True)
print(spam)
# 关于 sort
# 1. sort 对当前序列排序, 不返回新序列
# 2. 不能对既有数字又有字符串值得列表排序
# 3. sort 对字符串排序时, 使用"ASCII 字符顺序", 而不是实际的字典顺序
spam = ['a', 'Z', 'b', 'X']
spam.sort()
print(spam)
# key = str.lower : 按照普通字典顺序排序
# 这将导致 sort() 方法将列表中所有的表项当成小写, 但实际上并不会改变它们在列表中的值
spam.sort(key = str.lower)
print(spam)