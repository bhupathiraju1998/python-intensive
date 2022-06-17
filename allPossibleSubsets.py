def all_unique_combinations(words):
    words = sorted(set(words))
    n = len(words)
    all_combinations = {0:[[]]}
    for i in range(n):
        all_combinations[i+1] = []
        
        for combination in all_combinations[i]:
            for word in words:
                if(combination and word >combination[-1]) or len(combination) == 0:
                    all_combinations[i+1].append(combination+[word])
                    
    all_combinations.pop(0)
    return all_combinations
    

words = input().split()
all_combinations = all_unique_combinations(words)
for combinations in all_combinations.values():
    for combination in combinations:
        print(" ".join(combination))

