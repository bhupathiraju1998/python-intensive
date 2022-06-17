y = int(input())
if y == 1800:
    print("False")
elif ((y % 400) and (y % 100) and (y % 4)) == 0:
    print("True")
else:
    print("False")