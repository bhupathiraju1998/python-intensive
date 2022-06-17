a = input()
b = len(a)
sum = 0
for each in a:
    result = int(each) ** b
    sum = sum + result
if sum == int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    