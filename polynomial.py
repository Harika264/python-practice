import numpy as np

# Read coefficients as floats
coeff = list(map(float, input().split()))

# Read value of x
x = float(input())

# Evaluate polynomial at x
print(np.polyval(coeff, x))
