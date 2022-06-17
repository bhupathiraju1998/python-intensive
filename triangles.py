side_one = int(input())
side_two = int(input())
side_three= int(input())
if (side_three == side_two == side_one):
    print("Equilateral")
elif(side_one == side_two) or (side_two == side_three) or(side_three == side_one):
    print("Isosceles")
else :
    print("Scalene")