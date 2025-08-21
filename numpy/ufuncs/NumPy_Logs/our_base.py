from math import log
import numpy as np

nploog = np.frompyfunc(log, 2, 1)

print(nploog(100, 15))  # Base 15