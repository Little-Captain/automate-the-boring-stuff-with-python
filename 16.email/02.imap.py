#!/usr/bin/env python

# 正如 SMTP 是用于发送电子邮件的协议，因特网消息访问协议（IMAP）规定了如何
# 与电子邮件服务提供商的服务器通信，取回发送到你的电子邮件地址的电子邮件
# Python 带有一个 imaplib 模块，但实际上第三方的 imapclient 模块更易用
# imapclient 模块从 IMAP 服务器下载电子邮件，格式相当复杂。你很可能希望将
# 它们从这种格式转换成简单的字符串。pyzmail 模块替你完成解析这些邮件的辛苦工作
# 从终端窗口安装 imapclient 和 pyzmail36

# 用 IMAP 获取和删除电子邮件
# 在 Python 中，查找和获取电子邮件是一个多步骤的过程，需要第三方模块 imapclient 和 pyzmail
# 作为概述，一个完整的例子，包括登录到 IMAP 服务器，搜索电子邮件，获取它们，
# 然后从中提取电子邮件的文本

'''
'''

import imapclient
import sqlite3
import os
import sys

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
print(imapObj)

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
print(imapObj.login(username, password))

imapObj.logout()
