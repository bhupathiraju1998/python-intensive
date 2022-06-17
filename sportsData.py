students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
num = int(input())
for each in range(num):
    word = tuple(input().split())
    students_dict[word[0]] = word[1]
print(students_dict)