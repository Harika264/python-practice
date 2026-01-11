import numpy as np
n, m, p = map(int, input().split())

# Read first array (n rows, p columns)
arr1 = np.array([list(map(int, input().split())) for _ in range(n)])

# Read second array (m rows, p columns)
arr2 = np.array([list(map(int, input().split())) for _ in range(m)])

# Concatenate along axis 0 (rows)
result = np.concatenate((arr1, arr2), axis=0)

print(result)
