import numpy as np
arr = np.array([10,15,25,5])

newarr = np.diff(arr)
print(newarr)

newarr1 = np.diff(arr, n=2)
print(newarr1)

for i in range(len(arr)):
    print(np.diff(arr, n=i))