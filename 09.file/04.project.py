#!/usr/bin/env python

# 将带有美国风格日期的文件改名为欧洲风格日期
# 1 检查当前工作目录的所有文件名，寻找美国风格的日期。
# 2 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。
# 这意味着代码需要做下面的事情：
# 1 创建一个正则表达式，可以识别美国风格日期的文本模式。
# 2 调用 os.listdir()，找出工作目录中的所有文件。
# 3 循环遍历每个文件名，利用该正则表达式检查它是否包含日期。
# 4 如果它包含日期，用 shutil.move() 对该文件改名。

# 第 1 步：为美国风格的日期创建一个正则表达式
# 第 2 步：识别文件名中的日期部分
# 第 3 步：构成新文件名，并对文件改名
# 第 4 步：类似程序的想法
import shutil
import os
import re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    ''', re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # Form the European-style filename.
    euroFilename = '%s%s-%s-%s%s' % (beforePart, dayPart, monthPart, yearPart, afterPart)
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    # print('%s -> %s' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)