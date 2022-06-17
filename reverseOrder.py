k = int(input())
list_k = []

for i in range(k):
    val = input()
    list_k += [val]
for i in range(k):
    print(list_k[k-i-1])