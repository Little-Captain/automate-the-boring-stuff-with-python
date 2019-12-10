#!/usr/bin/env python

# csv 模块
# CSV 文件中的每行代表电子表格中的一行，逗号分割了该行中的单元格

# CSV 文件是简单的，缺少 Excel 电子表格的许多功能
# 1 值没有类型，所有东西都是字符串
# 2 没有字体大小或颜色的设置
# 3 没有多个工作表
# 4 不能指定单元格的宽度和高度
# 5 不能合并单元格
# 6 不能嵌入图像或图表

# CSV 的文件的优势是简单。CSV 文件被许多种类的程序广泛地支持，可以
# 在文本编辑器中查看，它是表示电子表格数据的直接方式
# CSV 格式和它声称的完全一致：它就是一个文本文件，具有逗号分隔的值
# 因为 CSV 文件就是文本文件，所以你可能会尝试将它们读入一个字符串，然后用字符串技术处理
# 因为 CSV 文件中的每个单元格有逗号分割，也许你可以只是对每行文本调用 split()方法，
# 来取得这些值。但并非 CSV 文件中的每个逗号，都表示两个单元格之间的分界。CSV 文件也有
# 自己的转义字符，允许逗号和其他字符作为值的一部分。split() 方法不能处理这些转义字符
# 因为这些潜在的缺陷，所以总是应该使用 csv 模块来读写 CSV 文件

# Reader 对象
# 要用 csv 模块从 CSV 文件中读取数据，需要创建一个 Reader 对象
# Reader 对象让你迭代遍历 CSV 文件中的每一行
import csv

'''
import pprint

exampleFile = open('example.csv', 'r')
exampleReader = csv.reader(exampleFile)
# 外层列表中存的是每行的值
# 每行的值也用列表存
exampleData = list(exampleReader)

pprint.pprint(exampleData)

exampleFile.close()

# csv 模块是 Python 自带的，所以不需要安装就可以导入它。
# 要用 csv 模块读取 CSV 文件，首先用 open()函数打开它，
# 就像打开任何其他文本文件一样。但是，不用在 open()返回
# 的 File 对象上调用 read() 或 readlines() 方法，而是
# 将它传递给 csv.reader() 函数。这将返回一个 Reader 对象，
# 供你使用。请注意，不能直接将文件名字符串传递给 csv.reader() 函数
# 要访问 Reader 对象中的值，最直接的方法，就是将它转换成一个
# 普通 Python 列表，即将它传递给 list()。在这个 Reader 对象上
# 应用 list() 函数，将返回一个列表的列表

# exampleData[row][col]
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[1][1])
print(exampleData[6][1])

print('--------------------')

# 在 for 循环中，从 Reader 对象读取数据
# 对于大型的 CSV 文件，你需要在一个 for 循环中使用 Reader 对象
# 这样避免将整个文件一次性装入内存
exampleFile = open('example.csv', 'r')

# 在导入 csv 模块，并从 CSV 文件得到 Reader 对象之后，可以循环
# 遍历 Reader 对象中的行。每一行是一个值的列表，每个值表示一个单元格
# Reader 对象只能循环遍历一次。要再次读取 CSV 文件，
# 必须调用 csv.reader，创建一个对象
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    # 要取得行号，就使用 Reader 对象的 line_num 变量，它包含了当前行的编号
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

exampleFile.close()
'''

'''
# Writer 对象
# Writer 对象让你将数据写入 CSV 文件。要创建一个 Writer 对象，
# 就使用 csv.writer() 函数
# Windows 下，需要为 open() 函数的 newline 关键字参数传入一个空字符串
# Linux 下，不需要
# 如果忘记设置 newline 关键字参数，output.csv 中的行距将有两倍
outputFile = open('output.csv', 'w') #, newline='')
outputWriter = csv.writer(outputFile)
# writerow 返回写入文件中这一行的字符数(包括换行符)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([0, 1, 2, 3.14159, 4])
outputFile.close()
# 请注意，Writer 对象自动转义了 'Hello, world!' 中的逗号，在 CSV 文件中使用了
# 双引号。模块 csv 让你不必自己处理这些特殊情况
'''

# delimiter 和 lineterminator 关键字参数
# 默认情况下，CSV 文件的分隔符是逗号。行终止字符是出现在行末的字符
# 默认情况下，行终止字符是换行符。你可以利用 csv.writer() 的 delimiter 和
# lineterminator 关键字参数，将这些字符改成不同的值
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
