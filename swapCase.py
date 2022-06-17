word = input()

mod_word = ""
for character in word:
    uppercase_char = character.upper()
    if uppercase_char == character:
        mod_word = mod_word + character.lower()
    else:
        mod_word = mod_word + character.upper()

print(mod_word)