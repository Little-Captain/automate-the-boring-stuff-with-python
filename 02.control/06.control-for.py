print('My name is')
# range(5): [0 5)
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

print('-------------------------------')

total = 0
for num in range(101):
    total += num
print(total)

print('-------------------------------')

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i += 1

for i in range(12, 16):
    print(i)

# range(start, end, step) [start end)
for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)