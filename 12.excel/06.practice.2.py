#!/usr/bin/env python

# 空行插入程序
# 创建一个程序 blankRowInserter.py，它接受两个整数和一个文件名字符串
# 作为命令行参数。我们将第一个整数称为 N，第二个整数称为 M。
# 程序应该从第 N 行开始，在电子表格中插入 M 个空行

import sys
import openpyxl

# 获取 N M excel 文件名
N = int(sys.argv[1])
M = int(sys.argv[2])
filename = sys.argv[3]

# 加载 excel 文件
wb = openpyxl.load_workbook(filename)
sheet = wb.active

# 插入空行
sheet.insert_rows(N, M)

# 保存 excel 文件
wb.save('inserted.xlsx')