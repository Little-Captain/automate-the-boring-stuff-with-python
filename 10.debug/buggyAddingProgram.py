#!/usr/bin/env python

import sys

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
try:
    sum = int(first) + int(second) + int(third)
except ValueError:
    sys.exit(-1)
print('The sum is %d' % sum)