num = int(input())
for each in range(1,(2*num)+2):
    if ((each == 1) or (each == num+1)) or (each == (2*num)+1):
        case_one = "* " * num
        print(case_one)
    else:
        case_one = "* "
        spaces = "  " 
        case_two = spaces * (num - 2)
        print(case_one + case_two + case_one)
        