#!/usr/bin/env python

# 多线程

'''
# 01
import time
import datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')
'''

# Python 程序在默认情况下，只有一个执行线程

# 不必让所有的代码等待，直到 time.sleep() 函数完成，可以使用 Python
# 的 threading 模块，在单独的线程中执行延迟或安排的代码。这个单独的线程
# 将因为 time.sleep() 调用而暂停。同时，程序可以在原来的线程中做其他工作

# 要得到单独的线程，首先要调用 threading.Thread() 函数，生成一个 Thread 对象

'''
# 02
import threading
import time
import datetime

print('%r Start of program.' % (datetime.datetime.now()))


def takeANap():
    time.sleep(5)
    print('%r Wake up!' % (datetime.datetime.now()))


# 函数也是对象
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('%r End of program.' % (datetime.datetime.now()))
'''

# 通常，单线程程序在文件中最后一行代码执行后终止(或调用 sys.exit())
# 在程序的所有线程终止之前，Python 程序不会终止
# 多线程程序，需要等待所有线程终止，Python 程序才会终止

# 向线程的目标函数传递参数
# 如果想在新线程中运行的目标函数有参数，可以将目标函数的参数传入 threading.Thread()
# 常规参数可以作为一个列表，传递给 threading.Thread() 中的 args 关键字参数
# 关键字参数可以作为一个字典，传递给 threading.Thread() 中的 kwargs 关键字参数
# 如果要向新线程中的函数传递参数，就使用 threading.Thread() 函数的 args 和 kwargs 关键字参数

# 03
import threading

print('Cats', 'Dogs', 'Frogs', sep=' & ')

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

# 并发问题
# 可以轻松地创建多个新线程，让它们同时运行。但多线程也可能会导致所谓的并发问题
# 如果这些线程同时读写变量，导致互相干扰，就会发生并发问题
# 并发问题可能很难一致地重现，所以难以调试
# 必须记住的是：为了避免并发问题，绝不让多个线程读取或写入相同的变量
# 当创建一个新的 Thread 对象时，要确保其目标函数只使用该函数中的局部变量
# 这将避免程序中难以调试的并发问题
