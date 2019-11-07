#!/usr/bin/env python

import re
import os

regex = re.compile(r'%s' % input('Please input a regex for search:\n'))

filenames = list(filter(lambda x: x.endswith('.txt'), os.listdir('.')))

for filename in filenames:
    with open(filename) as file:
        for line in file.readlines():
            if regex.search(line) != None:
                print(line)