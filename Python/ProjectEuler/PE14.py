# d = {1:0}
# 
# def CollatzSequence(num):
#     if num in d.keys():
#         return d[num]
#     
#     if num %2 == 0:
#         d[num] = 1 + CollatzSequence(num//2);
#     else:
#         d[num] = 1 + CollatzSequence(3 * num + 1);
#     
#     return d[num];
# 
# 
#      
# 
# for _ in range(int(input())):
#     i = int(input())
#     print(max(range(i+1,0,-1),key= CollatzSequence))



hailstone = lambda n: 3*n + 1 if n%2 else n//2

def d(n, _={1:1}):
    if n not in _: _[n] = d(hailstone(n)) + 1
    return _[n]

res = lambda L: max(range(L, 0,-1), key=d)

for _ in range(int(input())):
    i = int(input())
    print(res(i))