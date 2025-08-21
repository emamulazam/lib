import numpy as np

arr = np.array([3,6,9])

x = np.lcm.reduce(arr)

print(x)

arr1 = np.arange(1,11)
x1 = np.lcm.reduce(arr1)
print(x1)