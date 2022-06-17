num = int(input())
for each in range(1,num+1):
    i = num - (each-1)
    if i < num and i > 2:
        hollow_spaces = "  " * (i-2)
        numbers = "1 " + hollow_spaces + (str(i)+ " ")
        print(numbers)
    else:
        numbers = ""
        for j in range(1,i+1):
            numbers = numbers + (str(j)+" ")
        print(numbers)
 