#! python

# 4. 链接验证
# 编写一个程序，对给定的网页 URL，下载该页面所有链接的页面
# 程序应该标记出所有具有 404"Not Found" 状态码的页面，将它们作为坏链接输出

import requests
import bs4
import pprint

print('开始')

res = requests.get(r'http://www.allitebooks.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = list(filter(
    lambda x: type(x) == str and x.startswith('http://'),
    map(lambda x: x.get('href'), soup.select('a'))
))

pprint.pprint(links)

for link in links:
    if requests.get(link).status_code == 404:
        print('Bad Link %r' % link)
    else:
        print(link)

print('完成')
