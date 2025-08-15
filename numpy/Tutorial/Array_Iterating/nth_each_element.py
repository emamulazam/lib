import numpy as np
arr = np.array([[[1,2,3],[1,4,7]],
                [[9,5,1],[5,6,8]]])
for i in np.nditer(arr):
    print(i)