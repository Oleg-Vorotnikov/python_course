import pandas as pd
import numpy as np

# problem_1

df = pd.DataFrame(np.random.randint(0, 10, size=(10, 10)))

print(df)

# problem 2

df.index = list('ABCDEFGHIJ')

print(df)

df2 = df.loc[df[0] > 5]

for i in range(1, 9):
    df2 = df2.loc[df2[i] > 5]

print(df2)

# problem_3

df3 = pd.DataFrame(np.random.randint(0, 100, size=(10, 10)))

df3.index = list('ABCDEFGHIJ')
df3.columns = list('KLMNOPQRST')

print(df3)
print(df3.shape)
print(df3.columns)
print(df3.mean().mean())
df3.to_csv('df3.csv')
