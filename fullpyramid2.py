num = int(input())
sum = ""
k = 0
for each in range(1,num+1):
    k = num - each
    sum = sum + (str(each) + " ")
    result = " " * k + sum
    print(result)