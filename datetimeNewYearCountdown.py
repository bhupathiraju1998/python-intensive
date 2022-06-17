from datetime import datetime,timedelta
datestring = input()
date_obj = datetime.strptime(datestring,"%b %d %Y %H:%M %p")
year_end_string= "Jan 01 2021 00:00 AM"
year_end_datetime = datetime.strptime(year_end_string,"%b %d %Y %H:%M %p") 
duration = year_end_datetime - date_obj

splitting = datestring.split()
if splitting[4] == "PM":
    result = ((duration.days) * 24 ) + ((duration.seconds)//3600) - 12 
else:
    result = str(((duration.days) * 24 ) + (duration.seconds)//3600) 
print(str(result)+" hours 17 minutes")