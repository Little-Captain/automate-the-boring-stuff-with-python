#!/usr/bin/env python

# 旋转页面
# 利用 rotateClockwise() 和 rotateCounterClockwise() 方法，
# PDF 文档的页面也可以旋转 90 度的整数倍。向这些方法传入整数 90、180
# 或 270 就可以了。
import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

resultPdfFile = open('ratatePage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()