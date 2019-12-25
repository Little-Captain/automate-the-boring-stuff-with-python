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

print(imapObj.select_folder('INBOX', readonly=True))
UIDs = imapObj.search(['SINCE 05-07-2014'])
print(UIDs)

rawMessages = imapObj.fetch([4665], ['BODY[]', 'FLAGS'])
# print(rawMessages)

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessages[4665][b'BODY[]'])
print('-------------subject-------------')
print(message.get_subject())
print('-------------from-to-------------')
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))
print('-------------text_part-------------')
print(message.text_part != None)
print(message.text_part.get_payload().decode(message.text_part.charset))
print('-------------html_part-------------')
print(message.html_part != None)
print(message.html_part.get_payload().decode(message.html_part.charset))

imapObj.logout()
'''

# 连接到 IMAP 服务器
# 需要一个 IMAPClient 对象，连接到 IMAP 服务器并接收电子邮件
# 首先，需要电子邮件服务提供商的 IMAP 服务器域名得到 IMAP 服务器域名后
# 调用 imapclient.IMAPClient() 函数，创建一个 IMAPClient 对象
# 大多数电子邮件提供商要求 SSL 加密，传入 SSL=TRUE 关键字参数
import imapclient
import sqlite3
import os
import sys

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)

# 登录到 IMAP 服务器
# 取得 IMAPClient 对象后，调用它的 login() 方法
# 传入用户名（这通常是你的电子邮件地址）和密码字符串
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
# 要记住，永远不要直接在代码中写入密码
print(imapObj.login(username, password))

# 搜索电子邮件
# 登录后，实际获取感兴趣的电子邮件分为两步
# 首先，必须选择要搜索的文件夹
# 然后，必须调用 IMAPClient 对象的 search() 方法，传入 IMAP 搜索关键词字符串

# 选择文件夹
# 几乎每个账户默认都有一个 INBOX 文件夹，但也可以调用 IMAPClient 对象的
# list_folders() 方法，获取文件夹列表
# 这将返回一个元组的列表, 每个元组包含一个文件夹的信息
import pprint

pprint.pprint(imapObj.list_folders())

# 要选择一个文件夹进行搜索，就调用 IMAPClient 对象的 select_folder()
# 方法，传入该文件夹的名称字符串
# 如果所选文件夹不存在，Python 会抛出 imaplib.error 异常
# readonly=True 关键字参数可以防止你在随后的方法调用中，不小心更改或删除该文件夹中的任何电子邮件
# 除非你想删除的电子邮件，否则将 readonly 设置为 True 总是个好主意
print(imapObj.select_folder('INBOX', readonly=True))

# 执行搜索
# 文件夹选中后，就可以用 IMAPClient 对象的 search() 方法搜索电子邮件
# search() 的参数是一个字符串列表，每一个格式化为 IMAP 搜索键
# 在处理标志和搜索键方面，某些 IMAP 服务器的实现可能稍有不同

# 在传入 search() 方法的列表参数中，可以有多个 IMAP 搜索键字符串
# 返回的消息将匹配所有的搜索键。如果想匹配任何一个搜索键，使用 OR 搜索键
# 对于 NOT 和 OR 搜索键，它们后边分别跟着一个和两个完整的搜索键

# search() 方法不返回电子邮件本身，而是返回邮件的唯一整数 ID(UID)
# 然后可以将这些 UID 传入 fetch() 方法，获得邮件内容
UIDs = imapObj.search(['SINCE 05-07-2015'])
print(UIDs)

# 大小限制
# 如果你的搜索匹配大量的电子邮件，Python 可能抛出异常
# imaplib.error: got more than 10000 bytes
# 如果发生这种情况，必须断开并重连 IMAP 服务器，然后再试
# 这个限制是防止 Python 程序消耗太多内存
# 遗憾的是，默认大小限制往往太小
# 可以执行下面的代码，将限制从 10000 字节改为 10000000 字节
import imaplib

imaplib._MAXLINE = 10000000

# 取邮件并标记为已读
# 得到 UID 的列表后，可以调用 IMAPClient 对象的 fetch() 方法，获得实际的电子邮件内容
# UID 列表是 fetch() 的第一个参数。第二个参数应该是 ['BODY[]']，它告诉 fetch() 下载
# UID 列表中指定电子邮件的所有正文内容

# Gmail 专用
# UIDs = imapObj.gmail_search('meaning of life')
# print(UIDs)

rawMessages = imapObj.fetch(UIDs[0], ['BODY[]'])
pprint.pprint(rawMessages)
# 每条消息都保存为一个字典，包含两个键：'BODY[]' 和 'SEQ'
# 'BODY[]' 键映射到电子邮件的实际正文
# 'SEQ' 键是序列号，它与 UID 的作用类似
# 在 'BODY[]' 键中的消息内容是相当难理解的
# 这种格式称为 RFC822，是专为 IMAP 服务器读取而设计的

# 如果你选择一个文件夹进行搜索，就用 readonly=True 关键字参数来调用 select_folder()
# 这样做可以防止意外删除电子邮件，但这也意味着你用 fetch() 方法获取邮件时，它们不会标记为已读
# 如果确实希望在获取邮件时将它们标记已读，就需要将 readonly=False 传入 select_folder()
# 如果所选文件夹已处于只读模式，可以用另一个 select_folder() 调用重新选择当前文件夹
# 这次用 readonly=False 关键字参数

# 从原始消息中获取电子邮件地址

print(imapObj.logout())
