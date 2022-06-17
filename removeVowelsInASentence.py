string = input()

newstr = string;
#print("\nRemoving vowels from the given string");
vowels = ('a', 'e', 'i', 'o', 'u');
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"");
#print("New string after successfully removed all the vowels:");

capital_vowels = ('A', 'E', 'I', 'O', 'U');
for x in newstr:
    if x in capital_vowels:
        newstr = newstr.replace(x,"");
#print("New string after successfully removed all the vowels:");



print(newstr);