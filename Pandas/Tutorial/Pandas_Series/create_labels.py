import pandas as pd

a = [1,7,5]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar["y"])

print(myvar)
