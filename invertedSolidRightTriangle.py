num = int(input())
i = 0
for each in range(0,num):
    hollow_spaces = i  * " "
    i += 2
    print(hollow_spaces + ("* ") * (num - each))