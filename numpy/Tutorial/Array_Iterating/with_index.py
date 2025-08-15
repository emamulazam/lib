import numpy as np
arr = np.array([[1,3,2],[6,5,8]])
for ind, i in np.ndenumerate(arr):
    print(ind,i)