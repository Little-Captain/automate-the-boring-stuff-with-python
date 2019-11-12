#!/usr/bin/env python

# 如果 Python 遇到错误，它就会生成一些错误信息，称为“反向跟踪”
# 反向跟踪包含了出错消息、导致该错误的代码行号，以及导致该错误的函数调用的序列
# 这个序列称为“调用栈”

# 在从多个位置调用函数的程序中，调用栈就能帮助你确定哪次调用导致了错误


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


# spam()

# 只要抛出的异常没有被处理，Python 就会显示反向跟踪
# 但你也可以调用 traceback.format_exc()，得到它的字符串形式
# 如果你希望得到异常的反向跟踪的信息，但也希望 except 语句优雅地
# 处理该异常，这个函数就很有用。在调用该函数之前，
# 需要导入 Python 的 traceback 模块
import traceback

try:
    spam()
except Exception as err:
    print(str(err))
    print(traceback.format_exc())

