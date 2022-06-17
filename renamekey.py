fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
old_value = input()
new_value = input()
fruits_list = list(fruits.items())

fruits_list_copy = fruits_list
fruits_count = len(fruits_list)
for each in range(fruits_count):
    if fruits_list[each][0] == old_value:
        updated_tuple = (new_value,fruits_list[each][1])
        fruits_list_copy[each] = updated_tuple
print(fruits_list_copy)



