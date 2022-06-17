marks = float(input())
first_case = marks > 85
second_case = (marks > 70) and (marks <= 85)
third_case = (marks >= 60) and (marks <= 70)
fourth_case = marks < 60
if first_case:
    print("A")
elif second_case:
    print("B")
elif third_case:
    print("C")
elif fourth_case:
    print("F")