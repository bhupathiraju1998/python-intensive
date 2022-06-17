num = int(input())

for each in range(1,num+1):
    row = num - (each-1)
    sum = ""
    if row <= 2 or row == num:
        for i in range(1,row+1):
            sum = sum + str(i) + " "
            spaces = " " * (each-1)
        print(spaces+sum)
    else:
        spaces = " " * (each - 1)
        first_num = "1 "
        last_num = str(row) + " "
        hollow_spaces = "  " * (row-2)
        print(spaces+first_num+hollow_spaces+last_num)