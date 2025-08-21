import numpy as np

def myadd(a,b):
    return a+b

myadd = np.frompyfunc(myadd,2,1)

print(myadd([1,2,3,4],[5,6,7,8]))
print(type(myadd))