from collections import Counter
from optimus import optimus_compare as opticmp

def unoptimized(my_list) :
    new_list = []
    for i in set(my_list) :
        Count = my_list.count(i)
        new_list.append([i,Count])

    return sorted(new_list, key = lambda x: -x[1])

def optimized(my_list) :
    counter = Counter(my_list)
    return counter

s = [100, 23, 55, 103, 90, 68, 1]

print()
opticmp('unoptimized', 'optimized', (s, ), (s, ), verbose = True)
print()

