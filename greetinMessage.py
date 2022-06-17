time = int(input())
first_case = (time >= 4) and (time < 12)
second_case = (time >= 12) and (time < 16)
third_case = (time >= 16) and (time < 20)
fourth_case = (time >= 20) or (time < 4)
if first_case:
    print("Good Morning")
elif second_case:
    print("Good Afternoon")
elif third_case:
    print("Good Evening")
elif fourth_case:
    print("Good Night")