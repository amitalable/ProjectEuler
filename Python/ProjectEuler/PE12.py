import math
import time

def numberOfDivisor(_):
    count = 0
    for i in range(1,(int)(math.sqrt(_)) +1):
        if _ % i == 0:
            if _ // i == i:
                count +=1
            else:
                count +=2
    return count

def HighlyDivisibleTriangularNumber(n):
    for i in range(1,41041):
        if i %2 ==0:
            cnt = numberOfDivisor(i/2) * numberOfDivisor(i+1)
        else:
            cnt = numberOfDivisor(i) * numberOfDivisor((i+1)/2)
        if cnt > n:
            print((i * (i+1))//2)
            break;

for _ in range(int(input().strip())):
    n = int(input())
    start = time.time()
    HighlyDivisibleTriangularNumber(n)
    end = time.time()
    print("Runtime of the program is : ",end- start)