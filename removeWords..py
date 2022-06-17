word = input().split()
num = int(input())
final_string = []
for each in word:
    if len(each) != num:
        final_string.append(each)
final_string = " ".join(final_string)
print(final_string)