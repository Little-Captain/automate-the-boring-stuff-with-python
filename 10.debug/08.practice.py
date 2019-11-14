#!/usr/bin/env python

import random

coins = ('heads', 'tails')

guess = ''
while guess not in coins:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = coins[random.randint(0, 1)] # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are readlly bad at this game.')