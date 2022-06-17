month_list = ["January","February","March","April","May","June","July","August","September",
"October","November","December","Invalid Month Number"]
num = int(input())
if num <= 12:
    print(month_list[num-1])
else:
    print(month_list[12])