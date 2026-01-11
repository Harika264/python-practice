import numpy as np

# Read shape
shape = tuple(map(int, input().split()))

# Print zeros array
print(np.zeros(shape, dtype=int))

# Print ones array
print(np.ones(shape, dtype=int))
