#! python

# 2. 图像网站下载
# 编写一个程序，访问图像共享网站，如 Flickr 或 Imgur，查找一个类型的照片
# 然后下载所有查询结果的图像。可以编写一个程序，访问任何具有查找功能的图像网站

import requests
import os
import sys
import bs4

print('开始任务 👉👉👉👉👉')

# 搜索关键字
keywords = sys.argv[1]

# 生成文件的下载路径
os.makedirs(keywords, exist_ok=True)

baseURL = 'http://www.allitebooks.org/?s=%s' % keywords

res = requests.get(baseURL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

imgs = soup.select('img[class="attachment-post-thumbnail wp-post-image"]')
for img in imgs:
    link = img.get('src')
    filename = os.path.join(keywords, os.path.basename(link))
    downloadURL = 'axel -n 3 -a %r -o %r' % (link, filename)
    print('downloading %r' % downloadURL)
    os.system(downloadURL)
    print('downloaded')

print('完成任务 👌👌👌👌👌')
