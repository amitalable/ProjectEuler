def AbsDifference(num):
    sumOfSquare = 0
    for n in range(1,num+1):
        sumOfSquare += n*n
    squareOfSum = 0
    for n in range(1,num+1):
        squareOfSum += n
    return squareOfSum**2 - sumOfSquare

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(AbsDifference(n))