from functools import reduce

func = lambda num: reduce(lambda x,y: int(x)+int(y),str(num))

limit = 2**(10**4)

cache_List = [1]

for _ in range(1,(10**4)+1):
    cache_List.append(cache_List[-1]*2)

cache_List = list(map(func,cache_List))

T = int(input())

for _ in range(T):
    print(cache_List[int(input())])



