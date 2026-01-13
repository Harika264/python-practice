import numpy as np

# Read the dimension
n = int(input())

# Read first matrix
A = np.array([list(map(int, input().split())) for _ in range(n)])

# Read second matrix
B = np.array([list(map(int, input().split())) for _ in range(n)])

# Compute matrix multiplication (dot product)
result = np.dot(A, B)

# Print the result
print(result)
