number = int(input())

number1 = str(number)
first_number  = number1[0]
second_number = number1[1]
first_number_int = int(first_number)
second_number_int = int(second_number)
first_case = first_number_int + second_number_int == 7 
second_case = (first_number_int == 7) or(second_number_int == 7)
number = int(number)
multiple_7 = (number % 7 == 0)
if first_case:
    print("Special Number")
elif second_case:
    print("Special Number")
elif multiple_7:
     print("Special Number")
else:
    print("Normal Number")
    