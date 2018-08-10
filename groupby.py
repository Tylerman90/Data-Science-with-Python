import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

#in order to compute your data in the dataframe, you must store your groupby
#function within a variable.
byComp = df.groupby('Company')

#then you must call your aggregate method on that variable
#for mean
print(byComp.mean())

#for sum
print(byComp.sum())

#for standard deviations
print(byComp.std())

#you can even call your method on with conditions
print(byComp.sum().loc['FB'])

#but this is the legit way to call the output
print(df.groupby('Company').sum().loc['FB'])

#other useful aggregate fuctions
print(df.groupby('Company').count())
print(df.groupby('Company').max())
print(df.groupby('Company').min())

#the decribe method gives you a ton of useful information
print(df.groupby('Company').describe())

#you can even transpose it so that your dataframe is displayed differently
print(df.groupby('Company').describe().transpose())

#and of course you can also call column names off of this.
print(df.groupby('Company').describe().transpose()['FB'])