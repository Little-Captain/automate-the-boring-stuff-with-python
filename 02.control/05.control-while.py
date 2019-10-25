name = ''
while name != 'little captain':
    print('Please type your name.')
    name = input()
print('Thank you! %s' % name)

while True:
    print('Please type your name.')
    name = input()
    if name == 'lc':
        break
print('Thank you! %s' % name)

while True:
    print('Who are you?')
    name = input()
    if name != 'little captain':
        continue
    print('Hello, little captain. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
