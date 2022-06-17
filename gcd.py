num1 = int(input())
num2 = int(input())
for k in range(1,num2 +1):
    if (num1%k == 0) and (num2%k == 0):
        result = k
print(result)