#!/usr/bin/env python

# 用 zipfile 模块压缩文件
# 利用 zipfile 模块中的函数，Python 程序可以创建和打开（或解压）ZIP 文件

print('--------------------------------')

# 读取 ZIP 文件
# 要读取 ZIP 文件的内容，首先必须创建一个 ZipFile 对象（请注意大写首字母 Z 和F）。
# ZipFile 对象在概念上与 File 对象相似，要创建一个 ZipFile 对象，就调用 zipfile.ZipFile()函数，
# 向它传入一个字符串，表示 .zip 文件的文件名
# 请注意，zipfile 是 Python 模块的名称，ZipFile()是函数的名称

import zipfile, os

exampleZip = zipfile.ZipFile('zip.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()
# ZipFile 对象有一个 namelist() 方法，返回 ZIP 文件中包含的所有文件和文件夹的字符串的列表。
# 这些字符串可以传递给 ZipFile 对象的 getinfo() 方法，返回一个关于特定文件的 ZipInfo 对象。
# ZipInfo 对象有自己的属性，诸如表示字节数的 file_size 和 compress_size，它们分别表示
# 原来文件大小和压缩后文件大小。ZipFile 对象表示整个归档文件，而 ZipInfo 对象则保存该归档文件中
# 每个文件的有用信息

print('--------------------------------')

# 从 ZIP 文件中解压缩
# ZipFile 对象的 extractall() 方法从 ZIP 文件中解压缩所有文件和文件夹，放到当前工作目录中。
# 可以向 extractall() 传递的一个文件夹名称，它将文件解压缩到那个文件夹，而不是当前工作目录。
# 如果传递给 extractall() 方法的文件夹不存在，它会被创建
exampleZip1 = zipfile.ZipFile('zip.zip')
exampleZip1.extractall('./zip')
exampleZip1.close()
# ZipFile 对象的 extract() 方法从 ZIP 文件中解压缩单个文件
exampleZip2 = zipfile.ZipFile('zip.zip')
print(exampleZip2.extract('spam.txt', './zipone'))
exampleZip2.close()
# 传递给 extract() 的字符串，必须匹配 namelist() 返回的字符串列表中的一个

print('--------------------------------')

# 创建和添加到 ZIP 文件
# 要创建你自己的压缩 ZIP 文件，必须以"写模式"打开 ZipFile 对象，即传入 'w' 作为第二个参数
# 如果向 ZipFile 对象的 write() 方法传入一个路径，Python 就会压缩该路径所指的文件，
# 将它加到 ZIP 文件中。write() 方法的第一个参数是一个字符串，代表要添加的文件名。
# 第二个参数是“压缩类型”参数，它告诉计算机使用怎样的算法来压缩文件。
# 可以总是将这个值设置为zipfile.ZIP_DEFLATED（这指定了 deflate 压缩算法，它对各种类型的数据都很有效）
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
# 要记住，就像写入文件一样，写模式将擦除 ZIP 文件中所有原有的内容。
# 如果只是希望将文件添加到原有的 ZIP 文件中，就要向 zipfile.ZipFile() 传入 'a' 作为第二个参数，
# 以添加模式打开ZIP 文件。