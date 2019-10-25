# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')
# python2 python3 的 input 的区别
# python2 : input: 自动的识别输入的类型, 变量的类型即为识别的类型,
#                  如果接收的是数学计算式，会自动计算结果;
#           raw_input: 以str字符串类型输入
# python3 : input: 以str字符串类型输入, 
#                  即为 python2 中的 raw_input
myName = input() # 返回一个字符串
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')