def joinList(list):
    result = ''
    for i in range(len(list)):
        item = str(list[i])
        if i == len(list) - 1:
            result += 'and ' + item
        else:
            result += item + ', '
    return result

print(joinList([1, 2, 'list']))

print('---------------------------------')

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
    ]

row = len(grid)
column = len(grid[0])
for i in range(column):
    for j in range(row):
        print(grid[j][i], end='')
    print()