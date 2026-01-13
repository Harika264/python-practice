import numpy as np

# Read input arrays
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

# Compute and print inner product
print(np.inner(A, B))

# Compute and print outer product
print(np.outer(A, B))