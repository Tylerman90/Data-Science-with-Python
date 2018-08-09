import numpy as np
import pandas as pd


d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

#to drop null vaulues along rows. default axis=0
print(df.dropna())

#to drop null values along columns. argument axis=1
print(df.dropna(axis=1))

#set a threshold value that to determine atleast how many null values need to
#be present in order for your row or column to be dropped.
print(df.dropna(thresh=2))

#to fill in your null values
print(df.fillna(value='FILL VALUE'))

print(df['A'].fillna(value=df['A'].mean()))