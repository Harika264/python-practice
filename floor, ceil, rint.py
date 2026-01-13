import numpy as np

# IMPORTANT for correct output format
np.set_printoptions(sign=' ')

# Read input array
arr = np.array(list(map(float, input().split())))

# Print floor, ceil, and rint
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
