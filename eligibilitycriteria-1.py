m = int(input())
p = int(input())
c = int(input())
sum_of_mpc = m+p+c
if (m >= 70 and p >= 60 and c >= 60) or sum_of_mpc >= 180:
    print("True")
else:
    print("False")