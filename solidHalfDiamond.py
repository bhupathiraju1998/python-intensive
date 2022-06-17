num = int(input())
sum = ""
for each in range(1,num+1):
    sum =("* " *each)
    print(sum)
for i in range(1,num):
    row = num - (i-1)
    result = "* " * (row - 1)
    print(result)