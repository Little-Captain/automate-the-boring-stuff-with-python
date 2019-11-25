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

connect = sqlite3.connect(r'C:\Users\Little-Captain\.sqlite\lc.db')
cursor = connect.cursor()

username = '1203118412'
cursor.execute("select password from user where type = 'qq-mail' and username = %r" % username)
values = cursor.fetchall()
password = None
if len(values) == 1 and len(values[0]) == 1:
    password = os.popen('powershell encrypt -d %r' % values[0][0]).read()

if password == None:
    sys.exit(-1)

print(password)

# 