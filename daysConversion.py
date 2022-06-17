num = int(input())
year_count = 0
week_count = 0
day_count = 0
while num >= 365:
    num = num - 365
    year_count += 1 

while num > 7:
    num = num - 7
    week_count += 1

while num >  0:
    num = num - 1 
    day_count += 1
    
print(str(year_count) + " years " +str(week_count)+" weeks "+str(day_count)+" days" )
    
