a = int(input())
b = int(input())
c = int(input())
case1 = ((a+b)>c and (b+c)>a)
case2 = (case1 and (c+a)>b)
if case2:
    print("It's a Triangle")
else:
    print("It's not a Triangle")