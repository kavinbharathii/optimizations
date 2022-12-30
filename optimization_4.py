import sys
from optimus import optimus_compare as opticmp

def unoptimized(iterations) :
    user_data = [ i*i for i in range(iterations)]
    return sys.getsizeof(user_data) , 'bytes'


def optimized(iterations) :
    user_data = (i*i for i in range(iterations))
    return sys.getsizeof(user_data) , 'bytes'

print()
opticmp('unoptimized', 'optimized', (10_000, ), (10_000, ), verbose = True, space_opt = True)
print()

