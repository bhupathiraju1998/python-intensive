def get_score(word):
    final_dict = {}
    for each in word:
        pair = each.split(":")
        key,value = pair[0],int(pair[1])
        if key in final_dict:
            add_value = final_dict[key]
            final_dict[key] = add_value+value
        else:
            final_dict[key] = value
    return final_dict

word = input().split(",")
final_result = get_score(word)
item_final_result = final_result.items()
print(sorted(item_final_result))