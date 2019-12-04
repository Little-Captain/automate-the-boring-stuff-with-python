#!/usr/bin/env python

import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0) # 从 0 开始
print(pageObj.extractText())
# 在取得 Page 对象后，调用它的l extractText() 方法，返回该页文本的字符串。
# 文本提取并不完美：一些字符在函数返回的字符串中消失了，而且空格有时候也会没有
