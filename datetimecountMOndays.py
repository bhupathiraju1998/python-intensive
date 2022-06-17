from datetime import datetime
mond = 0
months = range(1,13)
year_1,year_2 = input().split()
for year in range(int(year_1),int(year_2)+1):
    for month in months:
        date_obj = datetime(year,month,1)
        name_weekday = datetime.strftime(date_obj,"%A")
        if name_weekday == "Monday":
            mond += 1 
print(mond)from datetime import datetime
mond = 0
months = range(1,13)
year_1,year_2 = input().split()
for year in range(int(year_1),int(year_2)+1):
    for month in months:
        date_obj = datetime(year,month,1)
        name_weekday = datetime.strftime(date_obj,"%A")
        if name_weekday == "Monday":
            mond += 1 
print(mond)