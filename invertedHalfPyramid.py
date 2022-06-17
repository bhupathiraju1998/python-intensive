num = int(input())
for each in range(num):
    pattern = ""
    k = num - each
    for i in range(1,k+1):
        pattern = pattern + (str(i)+ " ")
    print(pattern)
    
