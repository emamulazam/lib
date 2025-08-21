import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

x = np.prod(arr1)
print(x)

x1 = np.prod([arr1, arr2])
print(x1)

x2 = np.prod([arr1, arr2], axis=1)
print(x2)

x3 = np.cumprod(arr1)
print(x3)