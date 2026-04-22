from itertools import groupby
S = input().strip()
for k, g in groupby(S):
    print(f"({len(list(g))}, {k})", end=" ")
