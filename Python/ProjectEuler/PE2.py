#!/bin/python3

import sys

def fibonacciNumber(number):
    l=[1,2]
    for i in range(3,number+1):
        x = l[-1]+l[-2]
        if(x<number):
            l.append(x)
        else:
            break
    return l

def sumOfEvenFibonacciNumber(number):
    x = 0
    for num in fibonacciNumber(number):
        if num%2==0:
            x+= num
    return x

t = int(input().strip())
list1 = []
for a0 in range(t):
    n = int(input().strip())
    list1.append(n)

for a1 in range(t):
    print(sumOfEvenFibonacciNumber(list1[a1]))

