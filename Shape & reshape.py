import numpy as np

# Read input and convert to NumPy array of integers
arr = np.array(input().split(), int)

# Reshape into 3x3 matrix
print(arr.reshape(3, 3))
