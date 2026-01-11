# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read rows and columns
n, m = map(int, input().split())

# Read the matrix
arr = np.array([list(map(int, input().split())) for _ in range(n)])

# Print transpose
print(np.transpose(arr))

# Print flatten
print(arr.flatten())
