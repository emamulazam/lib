import pandas as pd

df = pd.read_csv('data.csv')

df.fillna({'Calories': 130}, inplace=True)

print(df.to_string())