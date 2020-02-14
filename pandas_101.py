# task 1- create pandas dataframe
import pandas as pd
import numpy as np
 #create sample dataframe
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5],[3, 4, np.nan, 1], [3, 4, 0, 1]], columns=list('ABCD'))
print(df.shape())
# task 2 dropping nan values

df.dropna(axis=1, how='all') #remve all column where all value is 'NaN' exists
df.dropna(axis=0, how='all') #remve all row where all value is 'NaN' exists
# how=any
df.dropna(thresh=2) #remve all row if there is non-'NaN' value is less than 2
df.dropna(axis=0, subset=['A']) #remove row where if there is any 'NaN' value in column 'A'
df.dropna(axis=1, subset=[1]) #remove column  if there is any 'NaN' value in index is '1'

