import time
import math

__author__ = 'Owain'


def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())

print(microtime())
print(microtime(True))
