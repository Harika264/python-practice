import numpy as np

# Read dimensions
n, m = map(int, input().split())

# Read arrays
a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(n)])

# Perform operations
print(a + b)
print(a - b)
print(a * b)
print(a // b)      # Integer division
print(a % b)
print(a ** b)
