#! python
# #!/usr/bin/env python

# 从 sys.argv 读取命令行参数
# 读取剪贴板内容
# 调用 webbrowser.open() 函数打开外部浏览器

# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.amap.com/search?query=%s' % address)

# 只要有一个URL，webbrowser 模块就可以让用户不必打开浏览器，而直接加载一个网站