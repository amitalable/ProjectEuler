# d = {1:0}
# def CollatzSequence(num):
#     if num in d.keys():
#         return d[num]
#     
#     if num %2 == 0:
#         d[num] = 1 + CollatzSequence(num//2);
#     else:
#         d[num] = 1 + CollatzSequence(3 * num + 1);  
#     return d[num];      
#  
# for _ in range(int(input())):
#     i = int(input("Enter"))
#     print(max(range(i+1,0,-1),key= CollatzSequence))
#    
   

T = int(input())
bound = 5*10**6
mem_List, cache_list = [0]*(bound+1), [(0,0)]*(bound+1)
mem_List[1], cache_list[1] = 1, (1,1)


def collatz_Solution(num):
    if num < bound:
        if mem_List[num]!= 0:
            return mem_List[num]
        elif num%2 == 0:
            mem_List[num] = 1 + collatz_Solution(num//2);
        else:
            mem_List[num] = 1 + collatz_Solution(3 * num + 1);
        return mem_List[num];
    else:
        if num %2 == 0:
            return 1+ collatz_Solution(num//2);
        else:
            return 1+ collatz_Solution(3 * num + 1);


max_index = 1
while(T):
    curr_index, num = 2, int(input())
    if max_index > curr_index:
        curr_index = max_index
    while curr_index<= num:
        collatz_Solution(curr_index)
        cache_list[curr_index] = (curr_index,mem_List[curr_index]) if cache_list[curr_index-1][1]<= mem_List[curr_index] else cache_list[curr_index-1];
        max_index = curr_index
        curr_index +=1
    print(cache_list[num][0])
    T -=1



