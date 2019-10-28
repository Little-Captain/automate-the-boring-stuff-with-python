print('Hello')
print('World')
# 大多数参数是由它们在函数调用中的位置来识别的
# “关键字参数”是由函数调用时加在它们前面的关键字来识别的
# 关键字参数通常用于可选变元
print('Hello', end = ' ')
print('World', end = '\n')

print('cats', 'dogs', 'mice', sep = ', ')