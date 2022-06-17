num = int(input())
sum = 0
for each in range(1,num+1):
     if (num % each == 0):
         sum = sum + each
print(sum)