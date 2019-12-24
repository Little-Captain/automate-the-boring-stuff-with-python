#!/usr/bin/env python

# SMTP
# 简单邮件传输协议（SMTP）是用于发送电子邮件的协议
# SMTP 规定电子邮件应该如何格式化、加密、在邮件服务器之间传递
# 以及在点击发送后，计算机要处理的所有其他细节
# Python 的 smtplib 模块将它们简化成几个函数
# SMTP 负责向别人发送电子邮件
# IMAP 负责取回发送给你的电子邮件

'''
# 发送电子邮件
import smtplib
import sqlite3
import os

# SMTP 服务器的端口是一个整数值，几乎总是 587，该端口由命令加密标准 TLS 使用
smtpObj = smtplib.SMTP('smtp.qq.com', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())

# 连接数据库获取邮箱登录密码
connect = sqlite3.connect(r'/mnt/c/Users/Little-Captain/.sqlite/lc.db')
cursor = connect.cursor()

username = '1203118412@qq.com'
cursor.execute(
    "select password from user where type = 'qq-mail' and username = %r" % username)
values = cursor.fetchall()
password = None
if len(values) == 1 and len(values[0]) == 1:
    password = os.popen('powershell.exe encrypt -d %r' % values[0][0]).read()

if password == None:
    sys.exit(-1)

print(smtpObj.login(username, password))

print(smtpObj.sendmail(username, 'littlecaptain@foxmail.com', 'Subject: So long.'))

smtpObj.quit()
'''

# 连接到 SMTP 服务器
# 得到电子邮件提供商的域名和端口信息后，调用 smtplib.SMTP() 创建一个 SMTP 对象
# 传入域名作为一个字符串参数，传入端口作为整数参数
# SMTP 对象表示与 SMTP 邮件服务器的连接，它有一些发送电子邮件的方法
import smtplib
import sqlite3
import os
import sys

smtObj = smtplib.SMTP('smtp.qq.com', 587)
print(type(smtObj))

# 如果 smtplib.SMTP() 调用不成功，该 SMTP 服务器可能不支持 TLS 端口 587
# 这时，需要利用 smtplib.SMTP_SSL() 和 465 端口，来创建 SMTP 对象
'''
smtObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
print(type(smtObj))
'''

# 对于你的程序，TLS 和 SSL 之间的区别并不重要
# 只需要知道你的 SMTP 服务器使用哪种加密标准，这样就知道如何连接它

# 发送 SMTP 的 “Hello” 消息
# 得到 SMTP 对象后，调用它的名字古怪的 EHLO() 方法，向 SMTP 电子邮件服务器“打招呼”
# 这种问候是 SMTP 中的第一步，对于建立到服务器的连接是很重要的
# 只要确保得到 SMTP 对象后，第一件事就是调用 ehlo() 方法，否则以后的方法调用会导致错误
print(smtObj.ehlo())
# 如果在返回的元组中，第一项是整数 250 (SMTP 中“成功”的代码)，则问候成功了

# 开始 TLS 加密
# 如果要连接到 SMTP 服务器的 587 端口（即使用 TLS 加密），接下来需要调用 starttls() 方法
# 这是为连接实现加密必须的步骤
# 如果要连接到 465 端口（使用 SSL），加密已经设置好了，你应该跳过这一步
print(smtObj.starttls())
# starttls() 让 SMTP 连接处于 TLS 模式。返回值 220 告诉你，该服务器已准备就绪

# 登录到 SMTP 服务器
# 到 SMTP 服务器的加密连接建立后，可以调用 login() 方法
# 用你的用户名（通常是你的电子邮件地址）和电子邮件密码登录

username = '1203118412@qq.com'
password = None
# 连接数据库获取邮箱登录密码
connect = sqlite3.connect(r'/mnt/c/Users/Little-Captain/.sqlite/lc.db')
cursor = connect.cursor()

cursor.execute(
    "select password from user where type = 'smtp-imap' and username = %r" % username)
values = cursor.fetchall()
if len(values) == 1 and len(values[0]) == 1:
    # 注意: 通过 popen 执行命令，获取命令的输出，末尾带有一个换行符。一定要使用 strip() 函数去掉
    #      不然会有一些莫名的 BUG
    # 其实简单的说就是：在命令行终端中执行的命令，在输出结果的同时，最后都会追加一个换行符！！！
    password = os.popen('encrypt.exe -d %r' % values[0][0]).read()

if password == None:
    sys.exit(-1)
else:
    password = password.strip()

print(username)
print(password)
print(smtObj.login(username, password))
# 传入电子邮件地址字符串作为第一个参数，密码字符串作为第二个参数, 返回值 235 表示认证成功
# 如果密码不正确，Python 会抛出 smtplib.SMTPAuthenticationError 异常

# 将密码放在源代码中要当心。如果有人复制了你的程序，他们就能访问你的电子邮件账户
# 调用 input()，让用户输入密码是一个好主意
# 每次运行程序时输入密码可能不方便，但这种方法不会在未加密的文件中留下你的密码
# 黑客或笔记本电脑窃贼不会轻易地得到它

# 发送电子邮件
# 登录到电子邮件提供商的 SMTP 服务器后，可以调用的 sendmail() 方法来发送电子邮件
print(smtObj.sendmail(username, 'littlecaptain@foxmail.com',
                      'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob'))
# sendmail() 方法需要三个参数
# 1 你的电子邮件地址字符串（电子邮件的“from”地址）
# 2 收件人的电子邮件地址字符串，或多个收件人的字符串列表（作为“to”地址）
# 3 电子邮件正文字符串
# 电子邮件正文字符串必须以'Subject: \n'开头，作为电子邮件的主题行
# '\n'换行符将主题行与电子邮件的正文分开
# sendmail() 的返回值是一个字典
# 对于电子邮件传送失败的每个收件人，该字典中会有一个键值对
# 空的字典意味着对所有收件人已成功发送电子邮件

# 从 SMTP 服务器断开
# 确保在完成发送电子邮件时，调用 quit() 方法。这让程序从 SMTP 服务器断开
print(smtObj.quit())
