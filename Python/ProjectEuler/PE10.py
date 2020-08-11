#!/bin/python3

import sys

N = 1000000
l = [True]*(N+1)
for i in range(4,N+1,2):
    l[i] = False
i = 3
l[0],l[1] = False,False
while i <= N ** 0.5:
    if l[i]:
        for j in range(2*i,N+1,i):
            l[j] = False
    i+=2
m = [0,0,2,5]
sum = 5
for i in range(4,len(l)):
    if l[i]:
        sum += i
    m.append(sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(m[n])



