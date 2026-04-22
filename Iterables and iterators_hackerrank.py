from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
combos = list(combinations(range(n), k))
favorable = 0
for c in combos:
    for index in c:
        if letters[index] == 'a':
            favorable += 1
            break
probability = favorable / len(combos)
print(f"{probability:.3f}")
