# Remember: In Lattice Paths,from any point to a point(p,q). 
#           The total number of possible path is p+q C pq
#           i.e, factorial(p+q)/ factorial(p)* factorial(q)
from math import factorial as fact
fun = lambda x,y: (fact(x+y)//( fact(x)* fact(y)))%(1000000007)

T = int(input())

for _ in range(T):
    m,n = map(int,input().split())
    print(fun(m,n))