import numpy as np
arr = np.array([[1,3,2],[6,5,8]])
for i in np.nditer(arr[:,::2]):
    print(i)