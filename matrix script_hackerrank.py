import re
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
decoded_string = ""
for j in range(m):
    for i in range(n):
        decoded_string += matrix[i][j]
pattern = r'(?<=\w)[!@#$%& ]+(?=\w)'
final_output = re.sub(pattern, ' ', decoded_string)

print(final_output)
