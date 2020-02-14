# task 1- create pandas dataframe
import pandas as pd
# task 2. read dataframe from CSV file
wine=pd.read_csv('data/winequality-red.csv', header=0)
print(wine.head())

# task 3. Inspect dataframe shape
shape = wine.shape()
print(shape)
# task 4. data access and dataframe slicing
chlorides=wine.loc[:,'chlorides'] # all rows in the one column
# task 5 access data in a set of columns
chlorides.to_csv('data/new_csv.csv')
# task 6, find the mean value of the chloride column
chlorides_mean = wine.chlorides.mean()
print(chlorides_mean)