# print(9*5*8*7)
# 3 -> 1,2,3
# 4 -> 1,4,3
# 5 -> 1,4,3,5
# 6 -> 1,4,3,5
# 7 -> 1,4,3,5,7
# 8 -> 1,3,5,7,8
# 9 -> 1,5,7,8,9
# 10-> 1,7,8,9,5
# 11-> 5,7,8,9,11
# 12-> 5,7,8,9,11
# 13-> 5,7,8,9,11,13
# 14-> 5,7,8,9,11,13
# 15-> 5,7,8,9,11,13
# 16-> 5,7,9,11,13,16


def PrimeFactor(num):
    d = dict()
    temp = num
    for i in range(2,temp):
        if num%i ==0:
            d[i] = 0
            while num%i ==0:
                num //= i
                d[i] +=1
        if num ==1:
            break
    if not d:
        d[num] = 1
    return d
def MinimumNumber(num):
    if num == 1:
        return num
    res = PrimeFactor(num)
    for i in range(num-1,1,-1):
        temp = PrimeFactor(i)
        for key,value in temp.items():
            if key in res.keys():
                if res[key] < temp[key]:
                    res[key] = temp[key]
            else:
                res[key] = temp[key]
    temp =1
    for i,j in res.items():
        temp *= i**j
    return temp
  
                
                
print(MinimumNumber(44))
# for i in range(1,11):
#     print(MinimumNumber(i),end =" ")
#     