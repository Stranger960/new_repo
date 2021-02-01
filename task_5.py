### item 5

from functools import reduce
lst = [k for k in range(100, 1001) if k % 2 == 0]
def mult(prev, new):
    return prev * new
print(reduce(mult, lst))