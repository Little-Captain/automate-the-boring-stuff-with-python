#!/usr/bin/env python

# 从人口普查电子表格文件中读取数据，并在几秒钟内计算出每个县的统计值
# 1 从 Excel 电子表格中读取数据
# 2 计算每个县中普查区的数目
# 3 计算每个县的总人口
# 4 打印结果
# 代码需要完成下列任务:
# 1 用 openpyxl 模块打开 Excel 文档并读取单元格
# 2 计算所有普查区和人口数据，将它保存到一个数据结构中
# 3 利用 pprint 模块，将该数据结构写入一个扩展名为 .py 的文本文件

# 第 1 步: 读取电子表格数据
# 第 2 步: 填充数据结构
# 第 3 步: 将结果写入文件

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}

# Fill in countryData with each country's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # Make sure the key for this state exists.
    # 如果键已经存在，setdefault() 不会做任何事情
    countryData.setdefault(state, {})
    # Make sure the key for this country in this state exists.
    countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})
    # Each row represents one census tract, so incrment by one.
    countryData[state][country]['tracts'] += 1
    # Increase the country pop by the pop in this census tract.
    countryData[state][country]['pop'] += int(pop)

# Open a new text file and write the contents of countryData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print('Done.')

import census2010

print(census2010.allData['AK']['Anchorage'])
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))

# 解析 Excel 电子表格的程序都有类似的结构：
# 它加载电子表格文件，准备一些变量或数据结构，然后循环遍历电子表格中的每一行
# 这样的程序可以做下列事情：
# 1 比较一个电子表格中多行的数据
# 2 打开多个 Excel 文件，跨电子表格比较数据
# 3 检查电子表格是否有空行或无效的数据，如果有就警告
# 4 从电子表格中读取数据，将它作为 Python 程序的输入