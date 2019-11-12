#!/usr/bin/env python

# 断言
# “断言”是一个心智正常的检查，确保代码没有做什么明显错误的事情
# 这些心智正常的检查由 assert 语句执行
# 如果检查失败，就会抛出异常
# 在代码中，assert 语句包含以下部分：
# 1. assert 关键字；
# 2. 条件（即求值为 True 或 False 的表达式）；
# 3. 逗号；
# 4. 当条件为 False 时显示的字符串。
# testStr = 'open1'
# assert testStr == 'open', 'assert false'

# 断言和异常的比较
# 在日常英语中，assert 语句是说：“我断言这个条件为真，如果不为真，程序中什么地方就有一个缺陷。”
# 不像异常，代码不应该用 try 和 except 处理 assert 语句。
# 如果 assert 失败，程序就应该崩溃。通过这样的快速失败，产生缺陷和你第一次注意到该缺陷之间的
# 时间就缩短了。这将减少为了寻找导致该缺陷的代码，而需要检查的代码量。
# 断言: 针对的是程序员的错误
# 异常: 针对的是用户的错误
# 对于那些可以恢复的错误，请抛出异常，而不是用 assert 语句检测它
# 在程序执行中尽早快速失败，可以省去将来大量的调试工作。

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

# 禁用断言
# 在运行 Python 时传入 -O 选项，可以禁用断言
# 如果你已完成了程序的编写和测试，不希望执行心智正常检测，从而减慢程序的速度，
# 这样就很好（尽管大多数断言语句所花的时间，不会让你觉察到速度的差异）。
# 断言是针对开发的，不是针对最终产品。当你将程序交给其他人运行时，它应该没有缺陷，
# 不需要进行心智正常检查。
# python -O 03.assert.py