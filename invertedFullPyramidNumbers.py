num = int(input())
for each in range(1,num+1):
    space = " " * (each - 1) 
    i = num - (each - 1)
    numbers = ""
    for j in range(1,i+1):
        numbers = numbers + (str(j)+" ")
    print(space + numbers)
    
    
