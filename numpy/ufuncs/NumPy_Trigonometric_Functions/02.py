import numpy as np

arr = np.array([90,180,270,360,80,150,260])
x = np.deg2rad(arr)
print(x)

y = np.rad2deg(x)
print(y)