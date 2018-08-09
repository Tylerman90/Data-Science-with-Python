import numpy as np
import pandas as pd


d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

#to drop null vaulues along rows. default axis=0
print(df.dropna())

#to drop null values along columns. argument axis=1
print(df.dropna(axis=1))