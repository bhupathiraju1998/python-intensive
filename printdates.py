from datetime import datetime,timedelta
input_date = datetime.strptime(input(),"%d %b %Y")
 
previous_day = input_date - timedelta(days = 1)
next_day = input_date + timedelta(days = 1)
print(previous_day)
print(input_date)
print(next_day)