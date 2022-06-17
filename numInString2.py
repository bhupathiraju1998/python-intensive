given_string = input().split()
num = []

for k in given_string:
    if k.isdigit():
       num.append(k) 
      
    else:
        li = ""
        for j in k:
            if j.isdigit():
                li += j
        if len(li) > 0 and li == "13":
            num.append(li[0])
            num.append(li[1])
        elif len(li) > 0:
            num.append(li)
            

        
                

new_list = []
for each in num:
    each = int(each)
    new_list.append(each)

print(sum(new_list))
avg = (sum(new_list))/len(new_list)
print(round(avg,2))