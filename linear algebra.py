import numpy as np

# Read dimension
n = int(input())

# Read matrix
A = np.array([list(map(float, input().split())) for _ in range(n)])

# Compute determinant
det = np.linalg.det(A)

# Print rounded to 2 decimal places
print(round(det, 2))
