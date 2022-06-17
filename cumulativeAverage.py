num = int(input())
sum = 0
for each in range(1,num+1):
    num = int(input())
    sum = sum + num
    avg = sum / each
    result = round(avg,3)
    print(result)