num1 = int(input())
num2 = int(input())
case1 = num1 % num2
case2 = num2 % num1
if case1 < case2:
    print(case1)
else:
    print(case2)