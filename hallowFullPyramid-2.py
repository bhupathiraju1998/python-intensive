num = int(input())
i = 1
for each in range(1,num+1):
    if each <= 2 or each == num:
        sum = ""
        spaces = num - each 
        final_spaces = " " * spaces
        for i in range(1,each+1):
            sum = sum + (str(i) +" ")
        print(final_spaces+sum)
    else:
        spaces = num - each
        final_spaces = " " * spaces
        first_num = "1 "
        last_num = str(each)
        hollow_spaces = " " * (2*(each-2))
        print(final_spaces+first_num+hollow_spaces+last_num)
        i = i + 2
        
        
        
        
        