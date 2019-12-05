#!/usr/bin/env python

# 创建 pdf
# 在 PyPDF2 中，与 PdfFileReader 对象相对的是 PdfFileWriter 对象
# 它可以创建一个新的 PDF 文件。但 PyPDF2 不能将任意文本写入 PDF，就像
# Python 可以写入纯文本文件那样。PyPDF2 写入 PDF 的能力，仅限于从其他
# PDF 中拷贝页面、旋转页面、重叠页面和加密文件
# 模块不允许直接编辑 PDF。必须创建一个新的 PDF，然后从已有的文档拷贝内容

# 一般处理方式:
# 1．打开一个或多个已有的 PDF(源 PDF)，得到 PdfFileReader 对象
# 2．创建一个新的 PdfFileWriter 对象
# 3．将页面从 PdfFileReader 对象拷贝到 PdfFileWriter 对象中
# 4．最后，利用 PdfFileWriter 对象写入输出的 PDF

# 创建一个 PdfFileWriter 对象，只是在 Python 中创建了一个代表 PDF 文档的值，
# 这并没有创建实际的 PDF 文件，要实际生成文件，必须调用 PdfFileWriter 对象的
# write() 方法

# 拷贝页面
# 可以利用 PyPDF2，从一个 PDF 文档拷贝页面到另一个 PDF 文档
# 这让你能够组合多个 PDF 文件，去除不想要的页面，或调整页面的次序
import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

