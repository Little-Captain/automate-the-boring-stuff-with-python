#!/usr/bin/env python

import PyPDF2

# 解密 PDF
# 某些 PDF 文档有加密功能，以防止别人阅读，
# 只有在打开文档时提供口令才能阅读

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)
try:
    _ = pdfReader.getPage(0)
except Exception as e:
    print(e)

print(pdfReader.decrypt('rosebud'))
print(pdfReader.numPages)

# 这里仍然报错，很迷惑!!!
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
