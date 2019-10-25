# print('I am' + 29 + ' years old.') # error
print('I am ' + str(29) + ' years old.')
# str()、int()和float()函数将分别求值为传入值的字符串、整数和浮点数形式
# int('99.99') # error
print(42 == '42') # False
print('42' == '42') # True
print(42 == 42.0) # True
print(42.0 == 0042.000) # True
# 虽然数字的字符串值被认为与整型值和浮点型值完全不同，但整型值可以与浮点值相等
# Python 进行这种区分，因为字符串是文本，而整型值和浮点型都是数字
# 数字之间可以相等, 文本之间可以相等