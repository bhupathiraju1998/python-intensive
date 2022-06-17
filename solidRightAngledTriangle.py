num = int(input())
for each in range(1,num+1):
    hollow_spaces = " " * ((num-each) *2)
    stars = "* " * each
    print(hollow_spaces + stars)