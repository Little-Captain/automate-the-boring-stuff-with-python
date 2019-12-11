#!/usr/bin/env python

# 取得当前的天气数据

# 程序将执行以下操作:
# 1 从命令行读取请求的位置
# 2 从 OpenWeatherMap.org 下载 JSON 天气数据
# 3 将 JSON 数据字符串转换成 Python 的数据结构
# 4 打印今天和未来两天的天气

# 代码需要完成以下任务:
# 1 连接 sys.argv 中的字符串，得到位置
# 2 调用 requests.get()，下载天气数据
# 3 调用 json.loads()，将 JSON 数据转换为 Python 数据结构
# 4 打印天气预报

# 第 1 步：从命令行参数获取位置
# 第 2 步：下载 JSON 数据
# 第 3 步：加载 JSON 数据并打印天气

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: 04.project.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://samples.openweathermap.org/data/2.5/weather?q=%s&appid=b6907d289e10d714a6e88b30761fae22' % location
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
w = weatherData['weather'][0]
t = weatherData['main']
print('Current weather in %s:' % location)
print('{}: {}'.format(w['main'], w['description']))
print('temp: {}({}-{})'.format(t['temp'], t['temp_min'], t['temp_max']))

# 可以创建类似程序，完成以下任务:
# • 收集几个露营地点或远足路线的天气预报，看看哪一个天气最好
# • 如果需要将植物移到室内，安排一个程序定期检查天气并发送霜冻警报
# • 从多个站点获得气象数据，同时显示，或计算并显示多个天气预报的平均值
