#! python

# 用 selenium 模块控制浏览器

# selenium 模块让 Python 直接控制浏览器，实际点击链接，
# 填写登录信息，几乎就像是有一个人类用户在与页面交互。
# 与 Requests 和 Beautiful Soup 相比，Selenium 允许你
# 用高级得多的方式与网页交互。但因为它启动了 Web 浏览器，
# 假如你只是想从网络上下载一些文件，会有点慢，并且难以在后台运行。

print('0 ------------------------')

# 启动selenium 控制的浏览器
from selenium import webdriver
import sys

# 需要将对应的 driver.exe 放入某个 PATH 目录. 如 Python.exe 所在的目录
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')

# 在页面中寻找元素
# WebDriver 对象有好几种方法，用于在页面中寻找元素
# 它们被分成 find_element_* 和 find_elements_* 方法
# find_element_* 方法返回一个 WebElement 对象，代表页面中匹配查询的第一个元素
# find_elements_* 方法返回 WebElement_* 对象的列表，包含页面中所有匹配的元素
# selenium 的 WebDriver 方法，用于寻找元素
# 方法名                                             返回的 WebElement 对象/列表
# browser.find_element_by_class_name(name)          # 使用 CSS 类 name 的元素
# browser.find_elements_by_class_name(name)
# browser.find_element_by_css_selector(selector)    # 匹配 CSS selector 的元素
# browser.find_elements_by_css_selector(selector)
# browser.find_element_by_id(id)                    # 匹配 id 属性值的元素
# browser.find_elements_by_id(id)
# browser.find_element_by_link_text(text)           # 完全匹配提供的 text 的 <a> 元素
# browser.find_elements_by_link_text(text)
# browser.find_element_by_partial_link_text(text)   # 包含提供的 text 的 <a> 元素
# browser.find_elements_by_partial_link_text(text)
# browser.find_element_by_name(name)                # 匹配 name 属性值的元素
# browser.find_elements_by_name(name)
# browser.find_element_by_tag_name(name)            # 匹配标签 name 的元素
# browser.find_elements_by_tag_name(name)           # (大小写无关，<a> 元素匹配 'a' 和 'A')
# 除了 *_by_tag_name() 方法，所有方法的参数都是区分大小写的
# 如果页面上没有元素匹配该方法要查找的元素，selenium 模块就会抛出 NoSuchElement 异常
# 如果你不希望这个异常让程序崩溃，就在代码中添加 try 和 except 语句

# 一旦有了 WebElement 对象，就可以读取对象属性，或调用对象方法

# WebElement 的属性和方法
# attribute or method      描述
# tag_name                 标签名，例如 'a' 表示 <a> 元素
# get_attribute(name)      该元素 name 属性的值
# text                     该元素内的文本，例如 <span>hello</span> 中的 'hello'
# clear()                  对于文本字段或文本区域元素，清除其中输入的文本
# is_displayed()           如果该元素可见，返回 True，否则返回 False
# is_enabled()             对于输入元素，如果该元素启用，返回 True，否则返回 False
# is_selected()            对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
# location                 一个字典，包含键 'x' 和 'y'，表示该元素在页面上的位置

print('1 ------------------------')

try:
    elem = browser.find_element_by_class_name('col-sm-12')
    print(type(elem))
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# 点击页面
# find_element_* 和 find_elements_* 方法返回的 WebElement 对象
# 有一个 click() 方法，模拟鼠标在该元素上点击。
# 这个方法可以用于链接跳转，选择单选按钮，点击提交按钮，或者触发该元素
# 被鼠标点击时发生的任何事情

print('2 ------------------------')

try:
    elem = browser.find_element_by_link_text("See what's new in the second edition.")
    elem.click()
except:
    print('element not found')

# 填写并提交表单
# 向 Web 页面的文本字段发送击键，只要找到那个文本字段的 <input> 或
# <textarea> 元素，然后调用 send_keys() 方法

print('3 ------------------------')

browser.get('http://www.allitebooks.org/')

try:
    elem = browser.find_element_by_id("s")
    elem.send_keys('Swift')
    elem.submit()
except:
    print('element not found')

print('4 ------------------------')

# 发送特殊键
# selenium 有一个模块，针对不能用字符串值输入的键盘击键
# 它的功能非常类似于转义字符。这些值保存在 selenium.webdriver.common.keys 模块的属性中
# 如果在程序顶部运行 from selenium.webdriver.common.keys import Keys
# 那么，原来需要写 from selenium.webdriver.common.keys 的地方，就只要写 Keys

# selenium.webdriver.common.keys 模块中常用的变量
# attribute                                          含义
# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT          键盘箭头键
# Keys.ENTER, Keys.RETURN                            回车和换行键
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP  Home 键、End 键、PageUp 键和 Page Down 键
# Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE          Esc、Backspace 和字母键
# Keys.F1, Keys.F2, ..., Keys.F12                    键盘顶部的 F1 到 F12 键
# Keys.TAB                                           Tab 键

from selenium.webdriver.common.keys import Keys
import time

# 如果光标当前不在文本字段中，按下 home 和 end 键，
# 将使浏览器滚动到页面的顶部或底部
try:
    # <html> 标签是 HTML 文件中的基本标签：HTML 文件的完整内容包含在
    # <html> 和 </html> 标签之内。调用 browser.find_element_by_tag_name('html')
    # 是向一般 Web 页面发送按键的好地方
    # 有时，当你滚动到该页的底部，新的内容就会加载，这可能会有用
    elem = browser.find_element_by_tag_name("html")
except:
    print('element not found')

elem.send_keys(Keys.END)
elem.send_keys(Keys.HOME)

# 点击浏览器按钮
# 利用以下的方法，selenium 也可以模拟点击各种浏览器按钮
# browser.back()    点击"返回"按钮
# browser.forward() 点击"前进"按钮
# browser.refresh() 点击"刷新"按钮
# browser.quit()    点击"关闭窗口"按钮
browser.back()
browser.forward()
browser.refresh()

browser.close()