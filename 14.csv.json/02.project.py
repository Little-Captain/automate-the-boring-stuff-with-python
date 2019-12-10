#!/usr/bin/env python

# 假设你有一个枯燥的任务，要删除几百 CSV 文件的第一行

# 该程序需要打开当前工作目录中所有扩展名为 .csv 的文件，
# 读取 CSV 文件的内容，并除掉第一行的内容重新写入同名的文件
# 这将用新的、无表头的内容替换 CSV 文件的旧内容

# 好习惯: 与往常一样，当你写程序修改文件时，一定要先备份这些文件，
# 以防万一你的程序没有按期望的方式工作。你不希望意外地删除原始文件

# 总的来说，该程序必须做到以下几点:
# 1 找出当前工作目录中的所有 CSV 文件
# 2 读取每个文件的全部内容
# 3 跳过第一行，将内容写入一个新的 CSV 文件
# 在代码层面上，该程序需要做到以下几点:
# 1 循环遍历从 os.listdir() 得到的文件列表，跳过非 CSV 文件
# 2 创建一个 CSV Reader 对象，读取该文件的内容，利用 line_num 属性确定要跳过哪一行
# 3 创建一个 CSV Writer 对象，将读入的数据写入新文件

# 第 1 步：循环遍历每个 CSV 文件
# 第 2 步：读入 CSV 文件
# 第 3 步：写入 CSV 文件，没有第一行

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        # Reader 对象的 line_num 属性可以用来确定当前读入的是 CSV 文件的哪一行
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

# 针对 CSV 文件写的程序类似于针对 Excel 文件写的程序，因为它们都是电子表格文件
# 可以编程完成以下任务
# 1 在一个 CSV 文件的不同行，或多个 CSV 文件之间比较数据
# 2 从 CSV 文件拷贝特定的数据到 Excel 文件，或反过来
# 3 检查 CSV 文件中无效的数据或格式错误，并向用户提醒这些错误
# 4 从 CSV 文件读取数据，作为 Python 程序的输入
