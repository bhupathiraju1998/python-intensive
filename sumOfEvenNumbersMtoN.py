num1= int(input())
num2 = int(input())
sum = 0
for each in range(num1,num2 +1):
    even = each % 2 == 0
    if even:
        sum = sum +each
print(sum)