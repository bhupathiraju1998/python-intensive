num = int(input())
sum = 0
for each in range(1,num+1):
    even = each %2 == 0
    if even:
        sum = sum + each
print(sum)