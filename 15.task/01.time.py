#!/usr/bin/env python

# time 模块
# 内置的 time 模块让 Python 程序能读取系统时钟的当前时间
# 在 time 模块中，time.time() 和 time.sleep() 函数是最有用的模块

# 1970 年 1 月 1 日 0 点，即协调世界时(UTC)
# time.time() 函数返回自那一刻以来的秒数，是一个浮点值
import time

# 返回值是 Unix 纪元的那一刻与 time.time() 被调用的那一刻之间的秒数
print(time.time())

# 纪元时间戳可以用于剖析代码，也就是测量一段代码的运行时间
# 如果在代码块开始时调用 time.time()，并在结束时再次调用
# 就可以用第二个时间戳减去第一个，得到这两次调用之间经过的时间。

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 10000000):
        product += 1
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % len(str(prod)))
print('Took %s seconds to calculate.' % (endTime - startTime))

# 另一种剖析代码的方法是利用 cProfile.run() 函数
# 与简单的 time.time() 技术相比，它提供了详细的信息
# cProfile 是一个模块

# time.sleep() 函数
