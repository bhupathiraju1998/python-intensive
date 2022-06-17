number = int(input())
first_case = (number % 11) == 0
second_case =((number)%11 == 1)
if first_case:
    print("Special Eleven")
elif second_case:
    print("Special Eleven")
else:
    print("Normal Number")