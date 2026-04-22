from itertools import combinations_with_replacement
s, k = input().split()
s_sorted = sorted(s)
k = int(k)
combinations = combinations_with_replacement(s_sorted, k)
for combo in combinations:
    print("".join(combo))
