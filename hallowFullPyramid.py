num = int(input())
sum = ""
for each in range(1,num+1):
    if each > 2 and each < num:
        hollow = num - each
        spaces = " " * hollow
        astrisk = "* "
        internal_hollow = "  " * (each -2)
        print(spaces+astrisk+internal_hollow+astrisk)
        
        
    else:
        sum =  ("*" + " ") * each
        row = num - (each)
        hollow = " " * row
        print(hollow+sum)
    
    
    
    
   
    