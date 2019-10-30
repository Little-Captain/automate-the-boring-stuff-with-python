# 嵌套的字典和列表
# 当你对复杂的事物建模时, 可能发现字典和列表中需要包含其他字典和列表
# 列表适用于包含一组有序的值, 字典适合于包含关联的键与值
allGuests = {
    'Alice': {
        'apples': 5, 'pretzels': 12
    },
    'Bob': {
        'ham sandwiches': 3, 'apples': 2
    },
    'Carol': {
        'cups': 3, 'apple pies': 1
    }
}

def totalBrough(guests, item):
    numBrought = 0
    for v in guests.values():
        numBrought += v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples ' + str(totalBrough(allGuests, 'apples')))
print(' - Cups ' + str(totalBrough(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrough(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrough(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrough(allGuests, 'apple pies')))