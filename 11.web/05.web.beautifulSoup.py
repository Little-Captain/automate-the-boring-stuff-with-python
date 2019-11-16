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
# noStarchSoup = bs4.BeautifulSoup(res.text)
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

# CSS 选择器操作
# 元素选择器         p              选择所有 <p> 元素
# id 选择器         #firstname      选择 id="firstname" 的所有元素
# 类选择器          .intro          选择 class="intro" 的所有元素
# 属性选择器         [attribute]    选择带有 target 属性所有元素

# 不同的选择器模式可以组合起来，形成复杂的匹配
# soup.select('p #author') 将匹配所有 id 属性为 author 的元素，只要它也在一个<p>元素之内
# select() 方法将返回一个 Tag 对象的列表，这是 Beautiful Soup 表示一个 HTML 元素的方式
# 针对 BeautifulSoup 对象中的 HTML 的每次匹配，列表中都有一个 Tag 对象
# 在该元素上调用 getText() 方法，返回该元素的文本，或内部的 HTML
# Tag 值可以传递给 str() 函数，显示它们代表的 HTML 标签
# Tag 值也可以有 attrs 属性，它将该 Tag 的所有 HTML 属性作为一个字典
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
print('----------------------------------')
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

print('-------------------')

# 通过元素的属性获取数据
# Tag 对象的 get() 方法让我们很容易从元素中获取属性值
# 向该方法传入一个属性名称的字符串，它将返回该属性的值
spamElem = exampleSoup.select('span')[0]
print(str(spamElem))
print(spamElem.get('id'))
print(spamElem.get('some_nonexistent_addr') == None)
print(spamElem.attrs)