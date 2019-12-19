#!/usr/bin/env python

# 多线程 XKCD 下载程序
# 多线程程序中有一些线程在下载漫画，同时另一些线程在建立连接，或将漫画图像文件写入硬盘
# 它更有效地使用 Internet 连接，更迅速地下载这些漫画

# 第 1 步: 修改程序以使用函数
# 第 2 步: 创建并启动线程
# 第 3 步: 等待所有线程结束

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        url = 'http://xkcd.com/{}'.format(urlNumber)
        print('Downloading page {}...'.format(url))
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects
for i in range(1, 1401, 100): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
# 调用 Thread 对象 join() 方法将阻塞，直到该线程完成
# 主线程可以调用其他每个线程的 join() 方法
# 阻塞等待所有下载线程完成
for downloadThread in downloadThreads:
    downloadThread.join()

# 所有的 join() 调用返回后，'Done.' 字符串才会打印，如果一个 Thread 对象已经完成
# 那么调用它的 join() 方法时，该方法就会立即返回
print('Done.')

