#! python

import requests

# 用 requests.get() 函数下载一个网页

# requests.get() 函数接受一个要下载的 URL 字符串。
# requests.get() 的返回值为一个 Response 对象，
# 其中包含了 Web 服务器对你的请求做出的响应。
res = requests.get('https://fex.bdstatic.com/hunter/alog/monkey.min.js')
# res = requests.get('https://fex.bdstaic.com/hunter/alog/monkey.js')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

# 检查错误

# 在 Response 对象上调用 raise_for_status() 方法。
# 如果下载文件出错，这将抛出异常。如果下载成功，就什么也不做。
# 总是在调用 requests.get() 之后再调用 raise_for_status()。
# 你希望确保下载确实成功，然后再让程序继续。
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)

# 将下载的文件保存到硬盘