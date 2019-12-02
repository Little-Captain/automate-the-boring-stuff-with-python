#!/usr/bin/env python

# 设置单元格的字体风格
# 设置某些单元格行或列的字体风格，可以帮助你强调电子表格中重点的区域
# 为了定义单元格的字体风格，需要从 openpyxl.styles 模块导入 Font() 和 Style() 函数
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello World!'
wb.save('styled.xlsx')

print('--------------------')

# Font 对象
# Font 对象的 style 属性影响文本在单元格中的显示方式
# 要设置字体风格属性，就向 Font() 函数传入关键字参数
# Font        style      属性的关键字参数
# name        字符串      字体名称，诸如'Calibri' 或 'Times New Roman'
# size        整型        字体大小点数
# bold        布尔型      True 表示粗体
# italic      布尔型      True 表示斜体

# 公式
# 公式以一个等号开始，可以配置单元格，让它包含通过其他单元格计算得到的值
# 利用 openpyxl 模块，用编程的方式在单元格中添加公式，就像添加普通的值一样
import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'
wb.save('writeFormula.xlsx')

print('--------------------')

# 如果你希望看到该公式的计算结果，而不是原来的公式，就必须将 load_workbook()
# 的 data_only 关键字参数设置为 True。这意味着 Workbook 对象要么显示公式，
# 要么显示公式的结果，不能兼得(但是针对一个电子表格文件，可以加载多个 Workbook 对象)

import openpyxl

wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wbFormulas.active
print(sheet['A3'].value)

print('--------------------')

wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = wbDataOnly.active
print(sheet['A3'].value) # 和上面的结果一样，不知道为什么

# Excel 公式为电子表格提供了一定程度的编程能力，但对于复杂的任务，很快就会失去控制
# Python 代码的可读性比 Excel 公式更好

# 调整行和列
# 设置行高和列宽
# 合并和拆分单元格
# 冻结窗格
# 图表
