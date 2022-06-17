n = int(input())
sum = 0
for each in range(1,n+1):
    if len(str(each))==1:
        sum = sum + 1 
    elif len(str(each)) == 2:
        sum += 2
    elif len(str(each)) == 3:
        sum += 3
    elif len(str(each)) == 4:
        sum += 4
    elif len(str(each)) == 5:
        sum += 5
    elif len(str(each)) == 6:
        sum += 6
print(sum)