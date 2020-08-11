
from functools import reduce


x = '''739671'''

def LargestProductInSeries(x,k):
    res = 0
    if k ==1:
        return max(list(map(int,x)))
    x = x.replace("\n", "")
    for i in range(len(x)-k+1):
        temp = reduce(lambda x,y:int(x)*int(y), x[i:i+k])
        if res <temp:
            res = temp
    return res


k = 1
num = x
print(LargestProductInSeries(num, k))
