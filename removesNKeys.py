alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

# Write your code here
word = input().split()
for each in word:
    if each in alphabets.keys():
        
        del alphabets[each]
print(alphabets)
    
    
    