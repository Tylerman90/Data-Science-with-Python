import pandas as pd

#import csv files
pd.read_csv('example.csv')
#import excel files

#import html files
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print(data)