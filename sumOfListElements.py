word = input()
result = word.split(" ")
final_result = 0
for each in result:
    final_result = final_result + int(each)
print(final_result)    