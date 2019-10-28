def collztz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

print('Enter number')
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Please enter a number')
        continue

number = collztz(number)
while number != 1:
    number = collztz(number)