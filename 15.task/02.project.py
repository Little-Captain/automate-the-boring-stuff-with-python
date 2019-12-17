#!/usr/bin/env python

# 超级秒表

# 总的来说，你的程序需要完成:
# 1 记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”
# 2 打印圈数、总时间和单圈时间
# 代码将需要完成以下任务：
# 1 在程序开始时，通过调用 time.time() 得到当前时间，将它保存为一个时间戳
#   在每个单圈开始时也一样。
# 2 记录圈数，每次用户按下回车键时加 1
# 3 用时间戳相减，得到计算流逝的时间
# 4 处理 KeyboardInterrupt 异常，这样用户可以按 Ctrl-C 退出

# 第 1 步：设置程序来记录时间
# 第 2 步：记录并打印单圈时间

import time

# Display the program's instructions

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #  reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
