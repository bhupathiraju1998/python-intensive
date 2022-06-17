num1= int(input())
num2 = int(input())
num3 = int(input())
sum = 0
for each in range(num2,num3 +1):
    total = each %  num1 == 0
    if total:
        sum = sum +each
print(sum)