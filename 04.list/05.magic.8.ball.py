import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful',
    ]

print(messages[random.randint(0, len(messages) - 1)])

# 可以在行末使用续行字符\, 将一条指令写成多行. 可以把\看成是'这条指令在下一行继续'.
# \续行字符之后的一行中，缩进并不重要
print('Four score and seven ' + \
    'years age ...')