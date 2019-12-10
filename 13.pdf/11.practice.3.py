#!/usr/bin/env python

# 暴力 PDF 口令破解程序
# 假定有一个加密的 PDF 文件，你忘记了口令，但记得它是一个英语单词
# 尝试猜测遗忘的口令是很无聊的任务。作为替代，你可以写一个程序，
# 尝试用所有可能的英语单词来解密这个 PDF 文件，直到找到有效的口令
# 这称为暴力口令攻击。从 http://nostarch.com/automatestuff/dictionary.txt
# 这个字典文件包含 44000 多个英语单词，每个单词占一行
# 利用文件读取技巧来读取这个文件，创建一个单词字符串的列表
# 然后循环遍历这个列表中的每个单词，将它传递给 decrypt() 方法，
# 如果这个方法返回整数 0，口令就是错的，程序应该继续尝试下一个口令
# 如果 decrypt() 返回 1，程序就应该终止循环，打印出破解的口令
# 你应该尝试每个单词的大小写形式(在我的笔记本上，遍历来自字典文件的
# 所有 88000 个大小写单词，只要几分钟时间。这就是不应该使用简单英语
# 单词作为口令的原因)

import PyPDF2

'''
# 加密
pdfFileObj = open('./ratatePage.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.encrypt('word')
for page in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page))
pdfOutput = open('./ratatePage_en.pdf', 'wb')
pdfWriter.write(pdfOutput)
# 读入的文件对象, 写入的文件对象: 都必须在文件写入完成后才能关闭, 不然会出现问题
# 文件打开了，就必须关闭，不管是读还是写
pdfFileObj.close()
pdfOutput.close()
'''

# 读取单词到一个 list
dictFileObj = open('./dictionary.txt', 'r')
words = list(map(lambda l: l.strip(), dictFileObj.readlines()))

# 读取 pdf 进行解密
pdfFileObj = open('./ratatePage_en.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for w in words:
    if pdfReader.decrypt(w.lower()) != 0:
        print('密码为: %r' % w.lower())
        break
    elif pdfReader.decrypt(w.upper()) != 0:
        print('密码为: %r' % w.upper())
        break
    else:
        print(w)
        continue

pdfFileObj.close()
