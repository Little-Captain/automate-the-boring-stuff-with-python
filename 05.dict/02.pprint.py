# pprint() 和 pformat() 函数, "漂亮打印" 函数
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for c in message:
    count.setdefault(c, 0)
    count[c] += 1

pprint.pprint(count)

print('---------------------------------')

# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))
print(pprint.pformat(count))