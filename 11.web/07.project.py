#!/usr/bin/env python
# #! python

# 程序要做的事:
# 1. 加载主页
# 2. 保存该页的漫画图片
# 3. 转入前一张漫画的链接
# 4. 重复直到第一张漫画
# 这意味着代码需要做下列事情:
# 1. 利用 requests 模块下载页面
# 2. 利用 Beautiful Soup 找到页面中漫画图像的 URL
# 3. 利用 iter_content() 下载漫画图像，并保存到硬盘
# 4. 找到前一张漫画的链接 URL，然后重复

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd
        # imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        # for chunk in res.iter_content(100000):
        #     imageFile.write(chunk)
        # imageFile.close()
        # 使用 axel 下载
        filename = os.path.join('xkcd', os.path.basename(comicUrl))
        downloadURL = 'axel -n 10 -a %r -o %r' % (comicUrl, filename)
        print('start %r' % downloadURL)
        os.system(downloadURL)
        print('end %r' % downloadURL)
    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')