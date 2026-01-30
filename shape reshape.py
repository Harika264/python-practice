import numpy as np

# Read input, split, and convert to integers
arr = list(map(int, input().split()))

# Convert to NumPy array and reshape to 3x3
result = np.array(arr).reshape(3, 3)

# Print the array
print(result)
