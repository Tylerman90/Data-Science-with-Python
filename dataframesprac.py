import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df[['W','Z']])

#Creating a new columns
df['new'] = df['W'] + df['Y']
print(df)

#to remove a column
df.drop('new',axis=1,inplace=True)
print(df)

#to remove a row
print(df.drop('E'))

#conditional selection that brings back boolean values
booldf = df > 0
print(booldf)
#conditional selection with bracket notation to bring back numbers
print(df[booldf])
