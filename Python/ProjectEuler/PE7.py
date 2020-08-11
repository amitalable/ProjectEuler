#!/bin/python3

import sys


def FindNthPrimeNumber(num = 200000):
    l = [True]*(num)
    i = 2
    while i<= num**0.5:
        if l[i]:
            for j in range(2*i,num,i):
                l[j] = False
        i+=1
    primeList =[]
    for i in range(len(l)):
        if l[i]:
            primeList.append(i)
    return primeList

primeList =FindNthPrimeNumber()
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeList[n-1])
    
