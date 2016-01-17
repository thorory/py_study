import math

def is_sqr(x):
    return int(math.sqrt(x)) == math.sqrt(x)

print filter(is_sqr, range(1, 101))
