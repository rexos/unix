from itertools import product
from wordlist import Pattern
from collections import OrderedDict

charset = 'abc'
pattern = '@@R@@@Q@F@@A'
prev = 0
perms = {}
pat = Pattern(pattern)
pat = pat.scan()

for ind, val in enumerate(list(pattern)):
    if val != '@' and not perms.get((ind-prev), None):
        perms[ind-prev] = list(product(charset, repeat=(ind-prev)))
        prev = ind + 1

def solve(data, composed='', prev=0):
    if data == {}:
        if perms.get(len(pattern)-prev, None):
            for word in perms[len(pattern) - prev]:
                print(composed+(''.join(list(word))))
        else:
            print( composed )
    else:
        num, val = data.popitem(last=False)
        for word in perms[num-prev]:
            solve( OrderedDict(data), composed + (''.join(list(word))) + val, num+1 )


solve(pat)
