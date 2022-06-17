def no_of_char(word):
    line_one= word.lower()
    uni_char = set(line_one)
    uni_char.discard(" ")
    for each in sorted(uni_char):
        print("{}: {}".format(each,line_one.count(each)))



word = input()
no_of_char(word)