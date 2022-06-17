num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
num = int(input())
for each in num_list:
    con = num in each
    if con:
        str_one = num_list.index(each)
        str_two = each.index(num)
        msg = "{} {}"
        print(msg.format(str_one,str_two))
        break