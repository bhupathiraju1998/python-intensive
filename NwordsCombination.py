def all_unique_combinations(words,n):
    words = sorted(set(words))
    old_combinations = [[]]
    for i in range(n):
        new_combinations = []
        for combination in old_combinations:
            for word in words:
                if (combination and word > combination[-1]) or len(combination) == 0:
                    new_combinations.append(combination + [word])
            old_combinations = new_combinations
    return new_combinations


words = input().split()
n = int(input())
all_combinations = all_unique_combinations(words,n)
for combination in all_combinations:
    print(" ".join(combination))