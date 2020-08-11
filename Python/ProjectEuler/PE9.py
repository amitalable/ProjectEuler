#!/bin/python3

import sys

def Triplets(limit):
    res = -1
    sq_Of_Limit = limit*limit
    twice_Limit = 2*limit
    for a in range(3,(limit//3)+1):
        b = (sq_Of_Limit - twice_Limit*a)//(twice_Limit - 2*a)
        c = limit - a - b
        if a*a + b*b == c*c:
            prod = a*b*c
            if prod>res:
                res = prod
    return res 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Triplets(n))
