#! python

# 3. 2048
# 2048 是一个简单的游戏，通过箭头向上、下、左、右移动滑块，让滑块合并
# 实际上，你可以通过一遍一遍的重复“上、右、下、左”模式，获得相当高的分数
# 编写一个程序，打开 https://gabrielecirulli.github.io/2048/ 上的游戏，
# 不断发送上、右、下、左按键，自动玩游戏。

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

html = browser.find_element_by_tag_name("html")

maxTimes = 30
playTimes = 0
while True:
    html.send_keys(Keys.UP)
    html.send_keys(Keys.RIGHT)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.LEFT)
    try:
        # 获取到 game-over 表示结束了
        # 1. 打印当前分数和最佳分数
        # 2. 点击 retry 按钮, 重新开始
        browser.find_element_by_css_selector(
            "[class='game-message game-over']"
        )  # 抛出异常表示没有获取到 game-over 元素，即没有结束
        current = browser.find_element_by_class_name('score-container')
        best = browser.find_element_by_class_name('best-container')
        # 这样做是为了保证获取到准确的分数，current 元素中包裹了子元素，直接获取到的 text 不是分数
        current = current.text.split('\n')[0]
        # 这一步的分割其实没有必要，best 元素中没有包裹子元素，直接获取到的 text 即为分数
        best = best.text.split('\n')[0]
        playTimes += 1
        print('%s   current:%s   best:%s' %
              (str(playTimes).rjust(6, ' '),
               current.rjust(6, ' '),
               best.rjust(6, ' ')))
        if playTimes == maxTimes:
            break
        retry = browser.find_element_by_class_name('retry-button')
        retry.click()
    except:
        continue

browser.close()
