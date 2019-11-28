#!/usr/bin/env python

# 使用 openpyxl 模块

import openpyxl
import pprint
import sys

# 打开 excel 文档
wb = openpyxl.load_workbook('example.xlsx')
pprint.pprint(type(wb))

print('----------------------')

# 获取工作表
sheetNames = wb.sheetnames
pprint.pprint(sheetNames)

print('----------------------')

if len(sheetNames) == 0:
    sys.exit()

sheet = wb[sheetNames[0]]
pprint.pprint(type(sheet))
pprint.pprint(sheet.title)

print('----------------------')

# 获取活动表
# 活动表是工作簿在 Excel 中打开时出现的工作表
anotherSheet = wb.active
pprint.pprint(type(anotherSheet))
pprint.pprint(anotherSheet.title)

# 从表格中取得单元格
