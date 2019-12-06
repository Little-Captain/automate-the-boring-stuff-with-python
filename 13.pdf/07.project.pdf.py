#!/usr/bin/env python

# 从多个 PDF 中合并选择的页面

# 定制需要合并到 PDF 中的页面

# 总的来说，该程序需要完成:
# 1. 找到当前工作目录中所有 PDF 文件
# 2. 按文件名排序，这样就能有序地添加这些 PDF
# 3. 除了第一页之外，将每个 PDF 的所有页面写入输出的文件
# 从实现的角度来看，代码需要完成下列任务:
# 1. 调用 os.listdir()，找到当前工作目录中的所有文件，去除掉非 PDF 文件
# 2. 调用 Python 的 sort() 列表方法，对文件名按字母排序
# 3. 为输出的 PDF 文件创建 PdfFileWriter 对象
# 4. 循环遍历每个 PDF 文件，为它创建 PdfFileReader 对象
# 5. 针对每个 PDF 文件，循环遍历每一页，第一页除外
# 6. 将页面添加到输出的 PDF
# 7. 将输出的 PDF 写入一个文件，名为 allminutes.pdf

import PyPDF2
import os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('./pdf'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

# 能够利用其他 PDF 文件的页面创建 PDF 文件，这让你的程序能完成以下任务:
# 1. 从 PDF 文件中截取特定的页面
# 2. 重新调整 PDF 文件中页面的次序
# 3. 创建一个 PDF 文件，只包含那些具有特定文本的页面。文本由 extractText() 来确定
