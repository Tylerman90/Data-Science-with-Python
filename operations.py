import numpy as np
import pandas as pd

#create a DataFrame
df = pd.DataFrame({'col1':[1,2,3,4],
				'col2':[444,555,666,444],
				'col3':['abc','def','ghi','xyz']})
print(df.head())

#to find all the unique values in column2
print(df['col2'].unique())

#to find the number of unique values in column2 use nunique()
print(df['col2'].nunique())

#if you would like the number of times the each value appears you can use this
print(df['col2'].value_counts())

#to create your own function
def times2(x):
	return x*2

#the apply function allows you to apply your own custom functions to your dataframes
print(df['col1'].apply(times2))

#you can also use the apply function to for strings, for example:
print(df['col3'].apply(len))

#the apply function is especially useful with lamda functions
print(df['col2'].apply(lambda x: x*2))