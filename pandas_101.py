# task 1- create pandas dataframe
import pandas as pd
import numpy as np
 #create sample dataframe
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5],[3, 4, np.nan, 1], [3, 4, 0, 1]], columns=list('ABCD'))
print(df.shape())
# task 2 dropping nan values

df.dropna(axis=1, how='all') #remve all column where all value is 'NaN' exists
df.dropna(axis=0, how='all') #remve all row where all value is 'NaN' exists

# task 3. read dataframe from CSV file
wine=pd.read_csv('data/winequality-red.csv', header=0)
print(wine.head())

# task 4. data access and dataframe slicing

chlorides=wine.loc[:,'chlorides'] # all rows in the one column
sulphurs=wine.loc[:,['free sulfur dioxide','total sulfur dioxide']] # all rows in the specified cols
# task 5 access data in a set of columns
acid_data=wine.loc[:,'fixed acidity':'residual sugar'] # all rows from colx to coly

# task 6 save new dataframe to csv
df.to_csv('data/new_csv.csv')