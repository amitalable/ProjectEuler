def PrimeFactor(num):
    return [i for i in range(101,999) if num%i == 0 and len(str(num//i)) == 3]

for _ in range(int(input())):
    n = (input())
    while len(n)==6:
        n = str(int(n)-1) 
        if(n == n[::-1]):
            l = PrimeFactor(int(n))
            if len(l)!= 0:
                print(n)
                break
            else:
                n = str(int(n)-1) 
        
