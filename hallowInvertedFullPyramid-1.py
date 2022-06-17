num = int(input())
for each in range(1,num+1):
    i = num - (each - 1)
    if i > 2 and i < num:
        astrisk = "* "
        hollow_spaces = "  " * (i-2)
        spaces = each - 1 
        final_spaces = " " * spaces
        print(final_spaces+astrisk+hollow_spaces+astrisk)
    else:
        astrisk = "* " * i 
        spaces = each - 1
        final_spaces = " " * spaces
        print(final_spaces+astrisk)