num = int(input())
for each in range(0,num):
    stars = "* " * (num-each)
    left_spaces = " " * each 
    print(left_spaces + stars)
for item in range(2,num+1):
    down_stars = "* " * (item)
    down_left_spaces = " " * (num-item)
    print(down_left_spaces + down_stars)