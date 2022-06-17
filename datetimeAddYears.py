from datetime import datetime,timedelta

input_date = datetime.strptime(input(),"%b %d %Y")
increment_year = timedelta(days = int(input()) * 365)
final_year = input_date + increment_year
print(final_year)
