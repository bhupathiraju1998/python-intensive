from datetime import datetime
date = input()
date_string = "%d %b %Y"
result = datetime.strptime(date , date_string) 
print(result)