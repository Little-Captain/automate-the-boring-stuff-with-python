#!/usr/bin/env python

# 日志
# 记日志是一种很好的方式，可以理解程序中发生的事，以及事情发生的顺序
# Python 的 logging 模块使得你很容易创建自定义的消息记录
# 这些日志消息将描述程序执行何时到达日志函数调用，并列出你指定的任何变量当时的值
# 另一方面，缺失日志信息表明有一部分代码被跳过，从未执行

# 启用 logging 模块，在程序运行时将日志信息显示在屏幕上
import logging

# 指定日志等级和格式
# level 级别及更高级的日志将被打印输出
logging.basicConfig(filename='log.txt',
                    level=logging.DEBUG,
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

# 不要用 print 调试
# log: 用于输入程序员调试代码时的一些有用信息
# print: 用于输入用户与程序交互时的一些有用信息
# log 可以很方便地被禁用 logging.disable(level). level 级别及更低级的日志都会被禁掉

# 日志级别
# DEBUG    logging.debug()    最低级别。用于小细节。通常只有在诊断问题时，你才会关心这些消息
# INFO     logging.info()     用于记录程序中一般事件的信息，或确认一切工作正常
# WARNING  logging.warning()  用于表示可能的问题，它不会阻止程序的工作，但将来可能会
# ERROR    logging.error()    用于记录错误，它导致程序做某事失败
# CRITICAL logging.critical() 最高级别。用于表示致命的错误，它导致或将要导致程序完全停止工作

# 将日志记录到文件
# logging.basicConfig() 函数接受 filename 关键字参数
# 指定后，日志将记录到这个文件中；不指定，日志将被打印到控制台中