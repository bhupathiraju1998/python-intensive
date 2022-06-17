import datetime
# Enter dates input format example: 8 Feb 2021
date_start_str = input()
date_end_str = input()
# convert string to date format 
date_start = datetime.datetime.strptime(date_start_str, '%d %b %Y')
date_end = datetime.datetime.strptime(date_end_str, '%d %b %Y')
# initialization of the initial number of weekends
day = datetime.timedelta(days=1)
count_saturday = 0
count_sunday = 0
# iteration over all dates in the range
while date_start <= date_end:
    if date_start.isoweekday() == 6:
        count_saturday += 1
    if date_start.isoweekday() == 7:
        count_sunday += 1
    date_start += day
# output a single line containing two space-separated integers
print("Saturday:",count_saturday)
print("Sunday:", count_sunday)