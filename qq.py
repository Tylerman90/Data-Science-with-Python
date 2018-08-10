import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
#but this is the legit way to call the output
print(df.groupby('Company').sum().loc['FB'])

#and of course you can also call column names off of this.
print(df.groupby('Company').describe().transpose()['FB'])