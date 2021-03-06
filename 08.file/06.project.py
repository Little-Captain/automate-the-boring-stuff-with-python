#!/usr/bin/env python

# .pyw 扩展名意味着 Python 运行该程序时，不会显示终端窗口

# 项目：多重剪贴板
# 针对要检查的关键字，提供命令行参数
# 1. 如果参数是 save，那么将剪贴板的内容保存到关键字
# 2. 如果参数是 list，就将所有的关键字拷贝到剪贴板
# 3. 否则，就将关键词对应的文本拷贝到剪贴板
# 这意味着代码需要做下列事情：
# 1. 从 sys.argv 读取命令行参数
# 2. 读写剪贴板
# 3. 保存并加载 shelf 文件

# 详细查看 mcb.pyw

# 第 1 步：注释和 shelf 设置
# 第 2 步：用一个关键字保存剪贴板内容
# 第 3 步：列出关键字和加载关键字的内容