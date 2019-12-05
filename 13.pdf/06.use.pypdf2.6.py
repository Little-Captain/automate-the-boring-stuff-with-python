#!/usr/bin/env python

# 加密 PDF
# PdfFileWriter 对象也可以为 PDF 文档进行加密

import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# 在调用 write() 方法保存文件之前，调用 encrypt() 方法，传入口令字符串
# PDF 可以有一个用户口令(允许查看这个 PDF)和一个拥有者口令(允许设置打印、
# 注释、提取文本和其他功能的许可)。用户口令和拥有者口令分别是 encrypt()的
# 第一个和第二个参数。如果只传入一个字符串给 encrypt()，它将作为两个口令
pdfWriter.encrypt('swordfish')

resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)

resultPdf.close()
