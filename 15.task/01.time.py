#!/usr/bin/env python

# time 模块
# 内置的 time 模块让 Python 程序能读取系统时钟的当前时间
# 在 time 模块中，time.time() 和 time.sleep() 函数是最有用的模块

# 1970 年 1 月 1 日 0 点，即协调世界时(UTC)
# time.time() 函数返回自那一刻以来的秒数，是一个浮点值
import time

'''
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

# 如果需要让程序暂停一下，就调用 time.sleep() 函数，并传入希望程序暂停的秒数
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# time.sleep() 函数将阻塞(也就是说，它不会返回或让程序执行其他代码)
# 直到传递给 time.sleep() 的秒数流逝

# 暂停 30 秒，推荐写法
# 这样可以 Ctrl-C 快速中断
# 如果在这 30 秒内的某个时候按 Ctrl-C，应该马上看到抛出 KeyboardInterrupt 异常
for i in range(30):
    time.sleep(1)
'''

# 数字四舍五入
# 用 Python 内置的 round() 函数按照指定的精度四舍五入到一个浮点数
# 只要传入要舍入的数字，再加上可选的第二个参数，指明需要传入到小数点后多少位
# 如果省略第二个参数，round() 将数字四舍五入到最接近的整数
now = time.time()
print(now)
print(round(now))
print(round(now, 2))
print(round(now, 4))
print(type(now))
print(type(round(now)))
print(type(round(now, 2)))
print(type(round(now, 4)))
# 有小数点的数，就是 float
# 没有小数点的数，就是 int
