#!/usr/bin/env python

import re

oldFile = open('old.txt', 'r')
newFile = open('new.txt', 'w')

text = oldFile.read()

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
keys = regex.findall(text)

for k in keys:
    print('Enter an %s:' % k.lower())
    v = input()
    text = text.replace(k, v, 1)

newFile.write(text)

oldFile.close()
newFile.close()