num = int(input())
sum = 0
for each in range(1,num):
     if (num % each == 0):
         sum = sum + each
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
            
         