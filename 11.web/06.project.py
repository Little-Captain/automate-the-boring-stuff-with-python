#! python

# 项目："I'm Feeling Lucky" Baidu 查找
# 只要在命令行中输入查找主题，就能让计算机自动打开浏览器，
# 并在新的选项卡中显示前面几项查询结果

# 从命令行参数中获取查询关键字
# 1. 取得查询结果页面
# 2. 为每个结果打开一个浏览器选项卡
# 这意味着代码需要完成以下工作：
# 1. 从 sys.argv 中读取命令行参数
# 2. 用 requests 模块取得查询结果页面
# 3. 找到每个查询结果的链接
# 4. 调用 webbrowser.open() 函数打开 Web 浏览器

# 第1步：获取命令行参数，并请求查找页面
# 第2步：找到所有的结果
# 第3步：针对每个结果打开 Web 浏览器

import requests, sys, webbrowser, bs4

print('Baidu...')
res = requests.get('http://www.baidu.com/s?wd=%s' % ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
bs4Html = bs4.BeautifulSoup(res.text)
elems = bs4Html.select('div .t a[href]')
count = min(5, len(elems))
# Open a browser tab for each result.
for i in range(count):
    webbrowser.open(elems[i].get('href'))