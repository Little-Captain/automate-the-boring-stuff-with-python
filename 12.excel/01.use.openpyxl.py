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
cell = sheet['A1']  # (A, 1)
pprint.pprint(type(cell))
pprint.pprint(cell.value)
cell = sheet['B1']
pprint.pprint(type(cell))
pprint.pprint(cell.value)

print('----------------------')

# Row 从 1 开始
# Column 从 A 开始
print('Row %s, Column %s is %s' % (str(cell.row), cell.column, cell.value))
print('coordinate %s' % str(cell.coordinate))

print('----------------------')

cell = sheet.cell(row=1, column=1)
pprint.pprint(type(cell))
pprint.pprint(cell.value)

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)

# 确定 sheet 大小

print('----------------------')

print('row %d column %d' % (sheet.max_row, sheet.max_column))

print('----------------------')

for i in range(1, sheet.max_row + 1):
    for j in range(1, sheet.max_column + 1):
        print('({}, {}) {}'.format(i, j, sheet.cell(i, j).value))

print('----------------------')

# 列字母和数字之间的转换
from openpyxl.utils import get_column_letter, column_index_from_string
print(get_column_letter(1))
print(get_column_letter(2))
print(get_column_letter(27))
print(get_column_letter(900))
print(get_column_letter(sheet.max_column))
print(column_index_from_string('A'))
print(column_index_from_string('AA'))

print('----------------------')

# 从表中取得行和列
# 可以将 Worksheet 对象切片，取得电子表格中一行、一列或一个矩形区域中的所有 Cell 对象
# 然后可以循环遍历这个切片中的所有单元格
pprint.pprint(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

print('----------------------')

# sheet.columns 返回的是生成器对象
# 使用 list 转换为列表对象
columns = list(sheet.columns)
pprint.pprint(columns[1])

for cell in columns[1]:
    print(cell.value)

print(columns[1][1].value)

rows = list(sheet.rows)
pprint.pprint(rows[1])

# 复习
# 工作簿、工作表、单元格
# 1．导入 openpyxl 模块
# 2．调用 openpyxl.load_workbook() 函数
# 3．取得 Workbook 对象
# 4．调用 get_active_sheet() 或 get_sheet_by_name() 工作簿方法
# 5．取得 Worksheet 对象
# 6．使用索引或工作表的 cell() 方法，带上 row 和 column 关键字参数
# 7．取得 Cell 对象
# 8．读取 Cell 对象的 value 属性