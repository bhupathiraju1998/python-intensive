number = int(input())
first_case = ((number % 9) == 0)
number1 = str(number)
first_number  = number1[0]
second_number = number1[1]
first_number_int = int(first_number)
second_number_int = int(second_number)
second_case = (first_number_int == 9) or(second_number_int == 9)
if first_case:
    print("Lucky Number")
elif second_case:
    print("Lucky Number")
else:
    print("Unlucky Number")