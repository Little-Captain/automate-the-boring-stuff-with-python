#!/usr/bin/env python

# PDF 偏执狂
# os.walk() 函数编写一个脚本，遍历文件夹中的所有 PDF(包含子文件夹)
# 用命令行提供的口令对这些 PDF 加密。用原来的文件名加上
# _encrypted.pdf 后缀，保存每个加密的 PDF。在删除原来的文件之前，
# 尝试用一个程序读取并解密该文件，确保它被正确的加密
# 然后编写一个程序，找到文件夹中所有加密的PDF 文件(包括它的子文件夹)
# 利用提供的口令，创建 PDF 的解密拷贝。如果口令不对，程序应该打印一条
# 消息，并继续处理下一个 PDF 文件
import os
import PyPDF2
import sys


def plainPdfList():
    pdfs = []
    for folderName, subfolders, filenames in os.walk('./pdf'):
        for filename in filenames:
            if not filename.endswith('.pdf') or filename.endswith('_encrypted.pdf'):
                continue
            pdfs.append(os.path.join(folderName, filename[:-4]))
    return pdfs


def encryptedList():
    pdfs = []
    for folderName, subfolders, filenames in os.walk('./pdf'):
        for filename in filenames:
            if not filename.endswith('_encrypted.pdf'):
                continue
            pdfs.append(os.path.join(folderName, filename[:-4]))
    return pdfs


def encrypt(pwd):
    for filename in plainPdfList():
        oldName = filename + '.pdf'
        newName = filename + '_encrypted.pdf'
        pdfFileObj = open(oldName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfWriter.encrypt(pwd)
        pdfOutput = open(newName, 'wb')
        pdfWriter.write(pdfOutput)
        # 读入的文件对象, 写入的文件对象: 都必须在文件写入完成后才能关闭, 不然会出现问题
        # 文件打开了，就必须关闭，不管是读还是写
        pdfFileObj.close()
        pdfOutput.close()


def canDecrypt(pwd):
    for filename in encryptedList():
        fName = filename + '.pdf'
        pdfFileObj = open(fName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if pdfReader.decrypt(pwd) == 0:
            print('decrypt error %r' % fName)
            pdfFileObj.close()
            return False
        else:
            pdfFileObj.close()
    return True


def removeUnnecessary():
    for filename in plainPdfList():
        os.unlink(filename + '.pdf')


def main():
    pwd = sys.argv[1]
    encrypt(pwd)
    if canDecrypt(pwd) == True:
        removeUnnecessary()


if __name__ == '__main__':
    main()
