# import sys
# 
# def PrimeFactor(num):
#     res = num
#     while num%2 == 0:
#         num//= 2
#         res = 2
#     i=3    
#     while(i*i<=num):
#         while num%i == 0:
#             num = num//i
#             res = num
#         if num == 1:
#             res = i
#             break
#         i = i+2
#     if res == 2 and num !=1:
#         res =  num
#     return res
# 
# 
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(PrimeFactor(n))


from math import sqrt
for _ in range(int(input())):
    maxi = -1
    n = int(input())
    temp = n
    for j in range(2,int(sqrt(temp))+1):
        while (n%j==0):
            if j > maxi:
                maxi = j
            n/=j
    if (n> 1 and n> maxi):
        maxi = n
    print(maxi)