from datetime import datetime,timedelta
date_format = "%b %d %Y %I:%M%p"
fianl_date = datetime.strptime(input(),date_format)
result = datetime.strftime(fianl_date,"%d/%m/%Y %H:%M:%S")
print(result)
two = datetime.timedelta(days = 2)
r = fianl_date - two
print(r)