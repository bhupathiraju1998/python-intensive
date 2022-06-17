n = int(input())
for row in range(1, n+1):
    i = n - (row-1)
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = ("* " + hollow_spaces + "* ")
        print(numbers)
    else:
        print("* " * i)

