import pandas as pd

#import csv files

#import excel files

#import html files
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print(data)