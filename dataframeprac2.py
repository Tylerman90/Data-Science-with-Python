import numpy as np
import pandas as pd

from numpy.random import randn
# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

#to grab outside index
print(df.loc['G1'])

#and you can keep getting more specific
print(df.loc['G1'].loc[1])

#to name the index
df.index.names = ['Groups','Num']
print(df)

#to grab a specific value in your multilevel dataframe
print(df.loc['G2'].loc[2]['B'])

#to grab a cross-section of your multi-level dataframe
print(df.xs(1,level='Num')) 