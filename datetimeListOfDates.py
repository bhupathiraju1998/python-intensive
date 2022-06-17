from datetime import datetime,timedelta
obj_1 = datetime.strptime(input(),"%b %d %Y")
obj_2 = datetime.strptime(input(),"%b %d %Y")
no_of_days = (obj_2 - obj_1).days

for each in range(no_of_days+1):
    print(obj_1 + timedelta(days = each))


