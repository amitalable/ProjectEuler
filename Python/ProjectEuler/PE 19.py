def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
def number_of_days(year,month):
    no_of_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    return 29 if(month == 2 and check_leap_year(year))\
        else no_of_days[month]
        

def get_days(year,month):
    prev_year = year - 1
    temp = prev_year // 400 + prev_year // 4 - prev_year // 100
    res = temp  + prev_year
    
    curr_month = 1
    while curr_month < month:
        res += number_of_days(year, curr_month)
        curr_month += 1
    
    return res % 7 

def get(year, month, offset, year1, month1):
    res = 1 if offset %7 == 6 else 0 
    temp = month1 
    while year1 < year or temp < month:
        offset = (offset + number_of_days(year1, temp)) % 7
        if offset % 7 == 6:
            res += 1
        temp += 1
        if temp == 13:
            temp = 1
            year1 += 1
    return res

def main():
    for _ in range(int(input())):
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
        
        if start[2] != 1:
            start[1] += 1
            start[2] = 1
            if start[1] == 13:
                start[0] += 1
                start[1] = 1
        
        before = (get_days(start[0], start[1]) - get_days(1900, 1) + 7) % 7
        print(get(end[0], end[1], before, start[0], start[1]))

main()  
