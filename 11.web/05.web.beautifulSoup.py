#! python

# 用 BeautifulSoup 模块解析 HTML
# Beautiful Soup 是一个模块，用于从 HTML 页面中提取信息

import requests, bs4

# 从 HTML 创建一个 BeautifulSoup 对象

# bs4.BeautifulSoup() 函数调用时需要一个字符串，其中包含将要解析的HTML
# bs4.BeautifulSoup() 函数返回一个 BeautifulSoup 对象
# res = requests.get('https://www.baidu.com')
# res.raise_for_status()
exampleFile = open('example.html')
noStarchSoup = bs4.BeautifulSoup(exampleFile)
print(type(noStarchSoup))

# 用 select() 方法寻找元素

# 针对你要寻找的元素，调用 method() 方法，传入一个字符串作为 CSS "选择器"
# 这样就可以取得 Web 页面元素。选择器就像正则表达式：它们指定了要寻找的模式
# CSS 选择器的例子
# soup.select('div')                   所有名为 <div> 的元素
# soup.select('#author')               带有 id 属性为 author 的元素
# soup.select('.notice')               所有使用 CSS class 属性名为 notice 的元素
# soup.select('div span')              所有在 <div> 元素之内的 <span> 元素
# soup.select('div > span')            所有直接在 <div> 元素之内的 <span> 元素，中间没有其他元素
# soup.select('input[name]')           所有名为 <input>，并有一个 name 属性，其值无所谓的元素
# soup.select('input[type="button"]')  所有名为 <input>，并有一个 type 属性，其值为 button 的元素
