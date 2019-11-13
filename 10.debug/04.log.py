#!/usr/bin/env python

# 日志
# 记日志是一种很好的方式，可以理解程序中发生的事，以及事情发生的顺序
# Python 的 logging 模块使得你很容易创建自定义的消息记录
# 这些日志消息将描述程序执行何时到达日志函数调用，并列出你指定的任何变量当时的值
# 另一方面，缺失日志信息表明有一部分代码被跳过，从未执行

# 启用 logging 模块，在程序运行时将日志信息显示在屏幕上
import logging

# 指定日志等级和格式
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# 调用打印日志方法
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s!)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s!)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# 不要用 print() 调试