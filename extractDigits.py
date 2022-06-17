word = input()
result = []
for each in word:
    if each.isdigit():
        result += [int(each)]
print(sum(result))
print(min(result))
print(max(result))