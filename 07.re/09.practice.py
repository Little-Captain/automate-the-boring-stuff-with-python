#!/usr/bin/env python

import re


def strongPwd(pwd):
    lengthRegex = re.compile(r'.{8,}')
    upperRegex = re.compile(r'.*[A-Z].*')
    lowerRegex = re.compile(r'.*[a-z].*')
    digitRegex = re.compile(r'.*[0-9].*')
    return (lengthRegex.search(pwd) != None) \
        and (upperRegex.search(pwd) != None) \
        and (lowerRegex.search(pwd) != None) \
        and (digitRegex.search(pwd) != None)

def strip2(origin, deal=None):
    if deal == None:
        return re.compile(r'^\s*(.*?)\s*$', re.DOTALL).sub(r'\1', origin)
    else:
        return re.compile(r'^(%s)*(.*?)(%s)*$' % (deal, deal), re.DOTALL).sub(r'\2', origin)



print(strongPwd('1R31r3123'))
print(strip2('sdfsdfsd sdfs fsdsdfsdfxsdf', 'sdf'))
print(strip2('111131251231adfa11111', '1'))
