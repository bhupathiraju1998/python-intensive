num = int(input())
first_line = "* " * (2*num)
print(first_line)
p = 2
for each in range(1,num):
    stars = "* " * (num - each )
    hollow_spaces_count = "  " * p
    print(stars+hollow_spaces_count+stars)
    p = p + 2
p = p - 2
for each in range(1,num):
    stars = "* " * (each)
    hollow_spaces_count = "  " * p 
    print(stars+hollow_spaces_count+stars)
    p = p - 2
first_line = "* " * (2*num)
print(first_line)