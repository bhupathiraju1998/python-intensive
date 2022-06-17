num_of_sides = int(input())
first_case = num_of_sides < 3 
second_case = num_of_sides == 3
third_case = num_of_sides  == 4
fourth_case = num_of_sides ==  5
fifth_case = num_of_sides > 5
if first_case:
    print("Not Polygon")
elif second_case:
    print("Triangle")
elif third_case:
    print("Quadrilateral")
elif fourth_case:
    print("Pentagon")
elif fifth_case:
    print("Big Polygon")