import random
# import random, sys, os, math
# from random import * # from 模块名 import 导入内容
# 使用这种形式的 import 语句，调用 random 模块中的函数时不需要 random. 前缀
# 使用完整的名称会让代码更可读，所以最好是使用普通形式的 import 语句

for i in range(15):
    # 1 2 3 随机
    print(random.randint(1, 3))