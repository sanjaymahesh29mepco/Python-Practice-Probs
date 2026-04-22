from itertools import product
k, m = map(int, input().split())
lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    squared_row = [(x**2) % m for x in row]
    lists.append(squared_row)
max_s = 0
for combo in product(*lists):
    current_sum = sum(combo) % m
    if current_sum > max_s:
        max_s = current_sum

print(max_s)
