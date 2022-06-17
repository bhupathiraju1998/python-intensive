def change_case(word):
    list_a = [word[0].lower()]
    for each in word[1:]:
        if each in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            list_a.append("_")
            list_a.append(each.lower())
        else:
            list_a.append(each)
    return "".join(list_a)
word = input()

print(change_case(word))