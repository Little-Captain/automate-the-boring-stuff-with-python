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
testStr = 'open1'
assert testStr == 'open', 'assert false'

# 断言和异常的比较
# 在日常英语中，assert 语句是说：“我断言这个条件为真，如果不为真，程序中什么地方就有一个缺陷。”
# 不像异常，代码不应该用 try 和 except 处理 assert 语句。
# 如果 assert 失败，程序就应该崩溃。通过这样的快速失败，产生缺陷和你第一次注意到该缺陷之间的
# 时间就缩短了。这将减少为了寻找导致该缺陷的代码，而需要检查的代码量。
# 断言: 针对的是程序员的错误
# 异常: 针对的是用户的错误
# 对于那些可以恢复的错误，请抛出异常，而不是用 assert 语句检测它