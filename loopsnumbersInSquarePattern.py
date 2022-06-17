num = int(input())
k = 1 
for each in range(1,num+1):
    pattern = ""
    for i in range(1,num+1):
        pattern = pattern + (str(k) + " ")
        k = k + 1 
    print(pattern)

