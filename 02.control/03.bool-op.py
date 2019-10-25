# 3 个布尔操作符（and、or 和not）用于操作布尔值
# and 和 or 操作符总是接受两个布尔值（或表达式），所以它们被认为是“二元”操作符
print(True and False)
print(True or False)
print(not True)
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 2) or (2 == 2))
# 优先级: not > and > or

# 在用于条件时，0、0.0、''（空字符串）被认为是 False，其他值都被认为是 True
# 编码中, 应尽量使用易于阅读的条件表达式