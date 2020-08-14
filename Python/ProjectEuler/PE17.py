word = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",
        10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
        16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
        30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",
        100:"Hundred", 1000:"Thousand", 1000000: "Million", 1000000000:"Billion"}
        

def number_To_Words(num):
    str_word = ""
    length = len(str(num))
    if length == 1:
        str_word += word[num]+" ";
    
    elif length == 2:
        if num <= 20:
            str_word +=  word[num] +" ";
        elif num < 30:
            str_word += word[20] + " " +  word[num-20] + " ";
        elif num == 30:
            str_word += word[30] + " ";
        elif num < 40:
            str_word += word[30] +" " + word[num-30] + " ";
        elif num == 40:
            str_word += word[40] + " ";
        elif num < 50:
            str_word += word[40] + " " +word[num-40] + " ";
        elif num == 50:
            str_word += word[50] + " ";
        elif num < 60:
            str_word += word[50] + " " +word[num-50] + " ";
        elif num == 60:
            str_word += word[60] + " ";
        elif num < 70:
            str_word += word[60] +" " + word[num-60] + " ";
        elif num == 70:
            str_word += word[70] + " ";
        elif num < 80:
            str_word += word[70] +" " + word[num-70] + " ";
        elif num == 80:
            str_word += word[80] + " ";
        elif num < 90:
            str_word += word[80] +" " + word[num-80] + " ";
        elif num == 90:
            str_word += word[90] + " ";
        else:
            str_word += word[90] +" " + word[num-90] + " ";
    
    elif length == 3:
        temp = num//100
        temp1=""
        temp1 += word[temp] +" " + word[100] + " " + number_To_Words(num - (temp * 100));    
        str_word = temp1

    elif length == 4 or length == 5 or length == 6:
        temp = num// 1000
        temp1 = ""
        temp1 += number_To_Words(temp) +" " + word[1000] + " " + number_To_Words(num - (temp * 1000));    
        str_word = temp1

    elif length == 7 or length == 8 or length == 9:
        temp = num//1000000
        temp1 =""
        temp1 += number_To_Words(temp) +" " + word[1000000] +" " + number_To_Words(num -(temp * 1000000));
        str_word = temp1
        
        
    elif length == 10 or length == 11 or length == 12:
        temp = num//1000000000
        temp1 =""
        temp1 += number_To_Words(temp) +" " + word[1000000000]+" "+ number_To_Words(num-(temp * 1000000000));
        str_word = temp1
    return str_word.strip()


T = int(input())
for _ in range(T):
    num = int(input())
    if num == 0:
        print("Zero")
    else:
        print(number_To_Words(num)) 
        
        
        
            
        
        

    