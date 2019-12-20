#!/usr/bin/env python

# 简单的倒计时程序
# 让我们来写一个倒计时程序，在倒计时结束时报警
# 总的来说，程序要做到:
# 1 从 60 倒数
# 2 倒数至 0 时播放声音文件(alarm.wav)
# 代码将需要做到以下几点:
# 1 在显示倒计时的每个数字之间，调用 time.sleep() 暂停一秒
# 2 调用 subprocess.Popen()，用默认的应用程序播放声音文件

# 第 1 步: 倒计时
# 第 2 步: 播放声音文件

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)

# 对于许多编程语言，包括 Python，Unix 纪元(1970 年 1 月 1 日午夜，UTC)是一个标准的参考时间
# 虽然 time.time() 函数模块返回一个 Unix 纪元时间戳(也就是自 Unix 纪元以来的秒数的浮点值)，
# 但 datetime 模块更适合执行日期计算、格式化和解析日期信息的字符串

# time.sleep() 函数将阻塞(即不返回)若干秒。它可以用于在程序中暂停

# threading 模块用于创建多个线程，如果需要下载多个文件或同时执行其他任务，这非常有用
# 但是要确保线程只读写局部变量，否则可能会遇到并发问题

# 最后，Python 程序可以用 subprocess.Popen() 函数，启动其他应用程序。命令行参数可以传递给
# Popen() 调用，用该应用程序打开特定的文档。另外，也可以用 Popen() 启动 start、open 或
# see 程序，利用计算机的文件关联，自动弄清楚用来打开文件的应用程序
# 通过利用计算机上的其他应用程序，Python 程序可以利用它们的能力，满足你的自动化需求
