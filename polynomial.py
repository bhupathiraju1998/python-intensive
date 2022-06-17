n = int(input())
updated_list = []
final_string = []
result= []
for each in range(n):
    given_string = input().split()
    m,n = given_string
    final_m = int(m)
    final_n = int(n)
    new_list = []
    new_list.append(final_m)
    new_list.append(final_n)
    updated_list.append(new_list)
leng_updated_list = len(updated_list)
updated_list.sort()
final_list = updated_list[::-1]

for power,coeff in final_list:
    if coeff == 0:
        continue
    else:
        if coeff < 0 or power < 0:
            string = "- {}x^{}".format(coeff,power)
            result.append(string)
        else:
            if power == 0:
                string = "+ {}".format(coeff)
                result.append(string)
            elif power == 1:
                string = "+ {}x".format(coeff)
                result.append(string)
            elif coeff == 1:
                string = "+ x^{}".format(power)
                result.append(string)
            else:    
                string = "+ {}x^{}".format(coeff,power)
                result.append(string)

updated_result = " ".join(result)


updated_result = updated_result.replace("- -","- ")
updated_result = updated_result.replace("x^0","")
updated_result = updated_result.replace("x^1","x")
updated_result = updated_result.replace("1x^2","x^2")
updated_result = updated_result.replace("1x^7","x^7")

updated_result = updated_result.replace(" + "," $ ")
updated_result = updated_result.replace("+ ","")
updated_result = updated_result.replace(" $ "," + ")
updated_result = updated_result.replace(" - "," # ")
updated_result = updated_result.replace("- ","-")
updated_result = updated_result.replace(" # "," - ")

print(updated_result)

    
    
    
    
    