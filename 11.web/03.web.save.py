#! python

# 可以用标准的 open() 函数和 write() 方法，将 Web 页面保存到硬盘中的一个文件
# 首先，必须用“写二进制”模式打开该文件，即向函数传入字符串'wb'，作为 open() 的第二参数
# 即使该页面是纯文本的，你也需要写入二进制数据，而不是文本数据，目的是为了保存该文本中的
# “Unicode 编码”。

# 为了将 Web 页面写入到一个文件，可以使用 for 循环和 Response 对象的 iter_content() 方法
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))
playFile.close()

# 下载并保存到文件的完整过程如下:
# 1．调用 requests.get() 下载该文件
# 2．用 'wb' 调用 open()，以写二进制的方式打开一个新文件
# 3．利用 Respose 对象的 iter_content() 方法做循环
# 4．在每次迭代中调用 write()，将内容写入该文件
# 5．调用 close() 关闭该文件