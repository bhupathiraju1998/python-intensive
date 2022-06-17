num = int(input())
p = -2
for each in range(1,(2*num) +1):
    if each == num:
        result = "* " * (2*num)
        print(result)
    else:
        if each < num:
            k = num - (each - 1)
            first_case = "* " * each
            last_case = "* " * each
            hollow_spaces = (2*k) + (2*(k-2))
            final_spaces = " " * hollow_spaces
            result = first_case+final_spaces+last_case
            print(result)
for i in range(num):
    first_case = "* " * (num - i)
    spaces = "  " * (2 * i)
    print(first_case+spaces+first_case)
    