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

#a subset of the dataframe where only rows in column W that are greater than 0 are returned.
resultdf = df[df['W']>0]
print(resultdf)

#you can grab a subset off of a subset for example:
print(resultdf['X'])

#but this the smoothest way to do this is by combuining the two steps.
print(df[df['W']>0]['X'])
#you can even do this with selecting multiple columns
print(df[df['W']>0][['Y','X']])

boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
#or all together
print(df[df['W']>0][['Y','X']])

