#!/usr/bin/env python

# PDF 偏执狂
# os.walk() 函数编写一个脚本，遍历文件夹中的所有 PDF(包含子文件夹)
# 用命令行提供的口令对这些 PDF 加密。用原来的文件名加上
# _encrypted.pdf 后缀，保存每个加密的 PDF。在删除原来的文件之前，
# 尝试用一个程序读取并解密该文件，确保它被正确的加密
# 然后编写一个程序，找到文件夹中所有加密的PDF 文件(包括它的子文件夹)
# 利用提供的口令，创建 PDF 的解密拷贝。如果口令不对，程序应该打印一条
# 消息，并继续处理下一个 PDF 文件