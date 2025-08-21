import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([9,5,1])

newarr = np.add(arr1, arr2)
print(newarr)

newarr1 = np.sum([arr1, arr2])
print(newarr1)

newarr2 = np.sum([arr1, arr2], axis=1)
print(newarr2)

newarr3 = np.cumsum([arr1, arr2])
print(newarr3)