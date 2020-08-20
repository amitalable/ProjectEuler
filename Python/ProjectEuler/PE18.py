def calculate_maximum_sum(list_of_rows):
    N = len(list_of_rows)
    row = N - 2
    while row >= 0:
        for i in range(len(list_of_rows[row])):
            list_of_rows[row][i] += max(list_of_rows[row+1][i],list_of_rows[row+1][i+1])
        row -=1  
    return list_of_rows[0][0]

T = int(input())

for _ in range(T):
    N = int(input())
    l1=[list(map(int,input().split())) for i in range(N)]
    print(calculate_maximum_sum(l1))
    
    
    