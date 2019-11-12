#!/usr/bin/env python

# 抛出异常
# 抛出异常使用 raise 语句。在代码中，raise 语句包含以下部分：
# 1 raise 关键字；
# 2 对 Exception 函数的调用；
# 3 传递给 Exception 函数的字符串，包含有用的出错信息。
# raise Exception('This is the error message.')

# 通常是调用该函数的代码知道如何处理异常，而不是该函数本身
# 所以你常常会看到 raise 语句在一个函数中，try 和 except 语句
# 在调用该函数的代码中
# 使用 try 和 except 语句，你可以更优雅地处理错误，而不是让整个程序崩溃

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))