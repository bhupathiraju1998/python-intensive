n = int(input())
updated_list = []
k = n
result= []
final_result_list_1 = []
for each in range(n):
    given_string = input().split()
    m,n = given_string
    final_m = int(m)
    final_n = int(n)
    new_list = []
    new_list.append(final_m)
    new_list.append(final_n)
    updated_list.append(new_list)
    final_result_list_1.append(final_n)
updated_list = updated_list[::-1]
final_string = ""
for power,h in updated_list:
    if power == 0 and h == 0:
        final_string += "0 + "
    elif power == 0 and h < 0:
        final_string += str(h)
    elif h < 0:
        final_string += str(h)+"x^"+ str(power)+" + "
    elif power == 0:
        final_string += str(h) 
    elif h == 0:
        continue
    elif power == 1:
        final_string += str(h)+"x"+" + "
    elif h == 1:
        final_string += "x^"+ str(power) + " + "
    
    else:
        final_string += str(h)+"x^"+ str(power)+" + "
final_string = final_string.replace("+ -","- ")
final_string = final_string.strip("+ ")
       
n2 = int(input())
updated_list2 = []
l = n2
result= []
final_result_list_2 = []
for each in range(n2):
    given_string2 = input().split()
    m2,n2 = given_string2
    final_m2 = int(m2)
    final_n2 = int(n2)
    new_list2 = []
    new_list2.append(final_m2)
    new_list2.append(final_n2)
    updated_list2.append(new_list2)
    final_result_list_2.append(final_n2)
updated_list2 = updated_list2[::-1]
final_string2 = ""
for power2,h2 in updated_list2:
    if power2 == 0 and h2 == 0:
        final_string2 += "0 + "
    elif power2 == 0 and h2 <0:
        final_string2 += str(h2)
    elif h2 < 0:
        final_string2 += str(h2)+"x^"+ str(power2)+" + "
    elif power2 == 0:
        final_string2 += str(h2) 
    elif h2 == 0:
        continue
    elif power2 == 1:
        final_string2 += str(h2)+"x"+" + "
    elif h2 == 1:
        final_string2 += "x^"+ str(power2) + " + "
    else:
        final_string2 += str(h2)+"x^"+ str(power2)+" + "
final_string2 = final_string2.replace("+ -","- ")
final_string2 = final_string2.strip("+ ")
       

        
new_dict = {}   

for items in updated_list:
    new_dict[items[0]] = items[1]
for values in updated_list2:
    if values[0] in new_dict.keys():
        new_dict[values[0]] += values[1]
    else:
        new_dict[values[0]] = values[1]
new_final_string_4 = ""



for k,l in sorted(new_dict.items(),reverse= True):
    if l == 0:
        continue
    elif l == 1 and k == 0:
        new_final_string_4 += "x + "
    elif k == 1:
        new_final_string_4 += str(l)+"x" + " + "
    elif k == 0:
        new_final_string_4 += str(l)
    elif l < 0:
        new_final_string_4 += "- "+str(l)+"x^"+str(k) + " + "
    
    else:
        new_final_string_4 += str(l)+"x^"+str(k) + " + "
new_final_string_4 = new_final_string_4.replace("+ - -","- ")
new_final_string_4 = new_final_string_4.replace(" + -"," - ")
new_final_string_4 = new_final_string_4.replace("- -","-")
#new_final_string_4 = new_final_string_4.replace(" -  - "," - ")
new_final_string_4 = new_final_string_4.replace("1x","x")
if new_final_string_4 == "":
    print(0)
else:
    print(new_final_string_4)
     
        
        
        
        
        
        
        
        
        
        
        
        
        