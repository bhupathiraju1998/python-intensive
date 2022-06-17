def generate_3_combinations(words):
    words = sorted(set(words))
    combinations_1 = []
    for word in words:
        combinations_1.append([word])
    combinations_2 = []
    
    for combination in combinations_1:
        for word in words:
            if word > combination[-1]:
                
                
                combinations_2.append(combination + [word])
    combinations_3 = []
    
    for combination in combinations_2:
        for word in words:
            if word > combination[-1]:
                combinations_3.append(combination + [word])
    return combinations_3
words = input().split()
all_combinations =  generate_3_combinations(words)
for combination in all_combinations:
    print(" ".join(combination))
