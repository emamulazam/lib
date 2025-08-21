import pandas as pd

df = pd.read_csv('data.csv')

# print(df)

# print(pd.options.display.max_rows)  # The number of rows returned is defined in Pandas option settings.

pd.options.display.max_rows = 1000
print(df)