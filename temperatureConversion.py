word = input()
leng_word = len(word)

if word[leng_word-1] == "F":
    number= word[:leng_word-1]
    cel = (float(number) -32)*5/9
    kel = cel + 273
    final_cel = round(cel,2)
    final_kel = round(kel,2)
    final_far = float(number)
    print(str(final_cel)+"C")
    print(str(final_far)+"F")
    print(str(final_kel)+"K" )
    
if word[leng_word-1] == "C":
    number= word[:leng_word-1]
    
    kel = float(number) + 273
    far = (9*float(number))/5 + 32
    final_far = round(far,2)
    final_kel = round(kel,2)
    final_cel = float(number)
    print(str(final_cel)+"C")
    print(str(final_far)+"F")
    print(str(final_kel)+"K" )
    
if word[leng_word-1] == "K":
    number= word[:leng_word-1]
    float_num = float(number)
    cel = float(number) - 273
    far = (9*(float_num-273)) / 5 +32
    final_far = round(far,2)
    final_cel = round(cel,2)
    final_kel = float(number)
    print(str(final_cel)+"C")
    print(str(final_far)+"F")
    print(str(final_kel)+"K" )