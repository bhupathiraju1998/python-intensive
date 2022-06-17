from datetime import datetime,timedelta

new_obj = datetime.strptime(input(),"%d %b %Y")
result = new_obj.strftime("%A")
print(result)