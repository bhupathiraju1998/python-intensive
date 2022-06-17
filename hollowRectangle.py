num1 = int(input())
num2 = int(input())
for each in range(1,num1+1):
    if (each == 1) or (each == num1):
        print("* " * num2 )
    else:
        print("* " + ("  " * (num2 -2)) + "*")

