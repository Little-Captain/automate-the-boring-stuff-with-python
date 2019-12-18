#!/usr/bin/env python

# time 模块用于取得 Unix 纪元时间戳，并加以处理。
# 如果以更方便的格式显示日期，或对日期进行算术运算就应该使用 datetime 模块
# datetime 模块有自己的 datetime 数据类型。datetime 值表示一个特定的时刻

import datetime
import time

print(datetime.datetime.now())

dt = datetime.datetime(2019, 12, 18, 8, 30, 20, 20)
print(dt)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# Unix 纪元时间戳可以通过 datetime.datetime.fromtimestamp()，转换为 datetime 对象
# datetime 对象的日期和时间将根据本地时区转换。
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))
# 表达式 datetime.datetime.now() 和 datetime.datetime.fromtimestamp(time.time())
# 做的事情相同，它们都返回当前时刻的 datetime 对象

# datetime 对象可以用比较操作符进行比较，弄清楚谁在前面
# 后面的 datetime 对象是“更大”的值
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)
print(halloween2015 > newyear2016)
print(newyear2016 > halloween2015)
print(newyear2016 != oct31_2015)

# timedelta 数据类型
# datetime 模块还提供了 timedelta 数据类型，它表示一段时间，而不是一个时刻
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

# 要创建 timedelta 对象，就用 datetime.timedelta() 函数。datetime.timedelta() 函数
# 接受关键字参数 weeks、days、hours、minutes、seconds、milliseconds 和 microseconds
# 没有 month 和 year 关键字参数，因为“月”和“年”是可变的时间，依赖于特定月份或年份
# timedelta 对象拥有的总时间以天、秒、微秒来表示。这些数字分别保存在 days、seconds 和
# microseconds 属性中。total_seconds()方法返回只以秒表示的时间。将一个 timedelta 对象传入
# str()，将返回格式良好的、人类可读的字符串表示
print(datetime.timedelta(hours=1).total_seconds())
print(datetime.timedelta(hours=2).total_seconds())
print(datetime.timedelta(hours=3).total_seconds())

# 算术运算符可以用于对 datetime 值进行日期运算
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=365)
print(dt + thousandDays)

# 利用 + 和 - 运算符，timedelta 对象与 datetime 对象或其他 timedelta 对象相加或相减
# 利用 * 和 / 运算符，timedelta 对象可以乘以或除以整数或浮点数
oct21st = datetime.datetime(2015, 10 ,21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - 2 * aboutThirtyYears)

# 暂停直至特定日期
# time.sleep() 方法可以暂停程序若干秒。利用一个 while 循环，可以让程序暂停，直到一个特定的日期
# halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
stopTime = datetime.datetime(2019, 12, 18, 9, 2, 50)
while datetime.datetime.now() < stopTime:
    time.sleep(1)

print(datetime.datetime.now())

# 将 datetime 对象转换为字符串
# Unix 纪元时间戳和 datetime 对象对人类来说都不是很友好可读。利用 strftime() 方法
# 可以将 datetime 对象显示为字符串。(strftime() 函数名中的 f 表示格式，format)
# strftime() 指令
# %Y                  带世纪的年份，例如'2014'
# %y                  不带世纪的年份，'00'至'99'（1970 至 2069）
# %m                  数字表示的月份, '01'至'12'
# %B                  完整的月份，例如 'November'
# %b                  简写的月份，例如 'Nov'
# %d                  一月中的第几天，'01' 至 '31'
# %j                  一年中的第几天，'001' 至 '366'
# %w                  一周中的第几天，'0'（周日）至 '6'（周六）
# %A                  完整的周几，例如 'Monday'
# %a                  简写的周几，例如 'Mon'
# %H                  小时（24 小时时钟），'00' 至 '23'
# %I                  小时（12 小时时钟），'01' 至 '12'
# %M                  分，'00' 至 '59'
# %S                  秒，'00' 至 '59'
# %p                  'AM' 或 'PM'
# '%%'                  就是 '%' 字符

# 向 strftime() 传入一个定制的格式字符串，其中包含格式化指定（以及任何需要的斜线、冒号等）
# strftime() 将返回一个格式化的字符串，表示 datetime 对象的信息
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I %M %p'))
print(oct21st.strftime("%B of '%y"))

# 将字符串转换成 datetime 对象
# 如果有一个字符串的日期信息，如 '2015/10/21 16:29:00'或'October 21, 2015'
# 需要将它转换为 datetime 对象，就用 datetime.datetime.strptime() 函数
# strptime() 函数与 strftime() 方法相反。定制的格式字符串使用相同的指令，像 strftime() 一样
# 必须将格式字符串传入 strptime()，这样它就知道如何解析和理解日期字符串
# strptime() 函数名中 p 表示解析，parse
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
# 带有日期信息的字符串必须准确匹配定制的格式字符串，否则 Python 将抛出 ValueError 异常

# 在 Python 中，日期和时间可能涉及好几种不同的数据类型和函数

# 时间的 3 种不同类型的值:
# 1 Unix 纪元时间戳（time 模块中使用）是一个浮点值或整型值，表示自 1970 年 1 月 1 日午夜 0 点（UTC）以来的秒数
# 2 datetime 对象（属于 datetime 模块）包含一些整型值，保存在 year、month、day、hour、minute 和 second 等属性中
# 3 timedelta 对象（属于 datetime 模块）表示的一段时间，而不是一个特定的时刻

# 时间函数及其参数和返回值:
# 1 time.time() 函数返回一个浮点值，表示当前时刻的 Unix 纪元时间戳
# 2 time.sleep(seconds) 函数让程序暂停 seconds 参数指定的秒数
# 3 datetime.datetime(year, month, day, hour, minute, second) 函数返回参数指定的时刻的 datetime 对象
#   如果没有提供 hour、minute 或 second 参数，它们默认为 0
# 4 datetime.datetime.now() 函数返回当前时刻的 datetime 对象
# 5 datetime.datetime.fromtimestamp(epoch) 函数返回 epoch 时间戳参数表示的时刻的 datetime 对象
# 6 datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds) 函数返回一个
#   表示一段时间的 timedelta 对象。该函数的关键字参数都是可选的，不包括 month 或 year
# 7 total_seconds() 方法用于 timedelta 对象，返回 timedelta 对象表示的秒数
# 8 strftime(format) 方法返回一个字符串，用 format 字符串中的定制格式来表示
# 9 datetime.datetime.strptime(time_string, format) 函数返回一个 datetime 对象，它的时刻由 time_string 指定
