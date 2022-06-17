import datetime

start_date = datetime.datetime(1970,1,1)
seconds = datetime.timedelta(seconds = int(input()))
result = start_date + seconds

print(result.strftime("%Y-%m-%d %H:%M:%S"))