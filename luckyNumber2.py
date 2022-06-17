number = int(input())
first_case = (number % 6) == 0
second_case = (number % 3) == 0
third_case = (number % 2) == 0
if first_case:
    print("Number is divisible by 6")
elif second_case:
    print("Number is divisible by 3")
elif third_case:
    print("Number is divisible by 2")
else :
    print("Number is not divisible by 2, 3 or 6")