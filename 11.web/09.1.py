#! python

# 1. 命令行邮件程序
# 编写一个程序，通过命令行接受电子邮件地址和文本字符串
# 然后利用 selenium 登录到你的邮件账号，将该字符串作为邮件，
# 发送到提供的地址（你也许希望为这个程序建立一个独立的邮件账号）
# 这是为程序添加通知功能的一种好方法
# 你也可以编写类似的程序，从 Facebook 或 Twitter 账号发送消息

# 从 sqlite 中获取邮箱用户的密码密码
import sqlite3
import os
import sys
import time
from selenium import webdriver

# 连接数据库获取邮箱登录密码
connect = sqlite3.connect(r'C:\Users\Little-Captain\.sqlite\lc.db')
cursor = connect.cursor()

username = '1203118412'
cursor.execute(
    "select password from user where type = 'qq-mail' and username = %r" % username)
values = cursor.fetchall()
password = None
if len(values) == 1 and len(values[0]) == 1:
    password = os.popen('powershell encrypt -d %r' % values[0][0]).read()

if password == None:
    sys.exit(-1)

# 驱动 chrome
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

# 选择 qq 登录
qqBtn = driver.find_element_by_id('qqLoginTab')
qqBtn.click()

# 切换到 login frame
driver.switch_to.frame('login_frame')

# 输入用户名和密码
userInput = driver.find_element_by_css_selector('input#u.inputstyle')
pwdInput = driver.find_element_by_css_selector('input#p.inputstyle.password')
userInput.send_keys(username)
pwdInput.send_keys(password)

# 点击登录按钮
loginBtn = driver.find_element_by_css_selector('input#login_button.btn')
loginBtn.click()

# 等待登录
time.sleep(5)

# 点击写信按钮
writeBtn = driver.find_element_by_css_selector('a#composebtn')
writeBtn.click()

# 选择 mainFrame
driver.switch_to.frame('mainFrame')

# 等待进入 mainFrame
time.sleep(5)

# 点击最近使用的邮箱地址
firstAddress = driver.find_element_by_css_selector("a.lm_addr")
firstAddress.click()

# 输入主题
subjectInput = driver.find_element_by_css_selector('input#subject')
subjectInput.send_keys('selenium test')

# 切换 frame 到正文所在的 frame
inputIframe = driver.find_element_by_class_name('qmEditorIfrmEditArea')
driver.switch_to.frame(inputIframe)

# 输入正文
textInput = driver.find_element_by_css_selector('body div')
textInput.send_keys('selenium test 正文')

# 切换回 mainFrame
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')

# 等待进入 mainFrame
time.sleep(5)

# 点击发送按钮
sendInput = driver.find_element_by_css_selector('a.btn_gray.btn_space')
sendInput.click()

# 关闭浏览器
driver.close()
