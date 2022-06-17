students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
word = input().split()
students_dict[word[0]] = word[1]
print(students_dict)