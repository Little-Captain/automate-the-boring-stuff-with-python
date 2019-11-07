#!/usr/bin/env python

# 项目：生成随机的测验试卷文件
# tasks:
# 1. 创建 35 份不同的测验试卷。
# 2. 为每份试卷创建 50 个多重选择题，次序随机。
# 3. 为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。
# 4. 将测验试卷写到 35 个文本文件中。
# 4. 将答案写到 35 个文本文件中。
# 这意味着代码需要做下面的事：
# 1. 将州和它们的首府保存在一个字典中。
# 2. 针对测验文本文件和答案文本文件，调用open()、write()和close()。
# 3. 利用 random.shuffle() 随机调整问题和多重选项的次序。

# 第 1 步：将测验数据保存在一个字典中
# 第 2 步：创建测验文件，并打乱问题的次序
# 第 3 步：创建答案选项
# 第 4 步：将内容写入测验试卷和答案文件
# see randomQuizGenerator.py