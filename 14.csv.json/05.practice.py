#!/usr/bin/env python

# Excel 到 CSV 的转换程序

# 使用 openpyxl 模块，编程读取当前工作目录中的
# 所有 Excel 文件，并输出为 CSV 文件

# 一个 Excel 文件可能包含多个工作表，必须为每个表创建一个 CSV 文件
# CSV 文件的文件名应该是 <Excel 文件名>_<表标题>.csv，其中
# <Excel 文件名> 是没有扩展名的 Excel 文件名
# <表标题> 是 Worksheet 对象的 title 变量中的字符串

import os

for excelFile in os.listdir('./xlsx'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = []  # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                # Append each cell's data to rowData.

                # Write the rowData list to the CSV file.

        csvFile.close()
