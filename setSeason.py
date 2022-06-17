month = int(input())
first_case = ((month==11) or month == 12) or month == 1 
second_case = month == 2 or month == 3
third_case = ((month == 4) or month == 5) or month == 6
fourth_case  = month == 7 or month == 8 
fifth_case  = month == 9 or month == 10
if first_case:
    print("Winter")
elif second_case:
    print("Spring")
elif third_case:
    print("Summer")
elif fourth_case:
    print("Rainy")
elif fifth_case:
    print("Autumn")