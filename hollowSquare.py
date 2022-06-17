num = int(input())

for each in range(1,num+1):
    if (each == 1) or (each == num):
        print("* " * num )
    else:
        print("* " + ("  " * (num -2)) + "*")

