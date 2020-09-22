from math import factorial 
from functools import reduce
def sum_of_factorial(num):
    res = factorial(num)
    res = reduce(lambda x,y: int(x) + int(y), str(res))
    return res

for i in range(int(input())):
    x = int(input())
    print(sum_of_factorial(x))
