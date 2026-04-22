import numpy as np
n = int(input())
matrix = np.array([list(map(float, input().split())) for _ in range(n)])
det = np.linalg.det(matrix)
print(round(det, 2))
