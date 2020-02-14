import os
from test_folder.utils import get_calls
import pandas_101
import pandas as pd
wine=pd.read_csv('data/winequality-red.csv', header=0)
chloride_test=wine.loc[:,'chlorides'] # all rows in the one column
print(get_calls(pandas_101)[0])
def test_task1():
    assert 'pd' in dir(pandas_101), 'Have you imported the`pandas` library with an alias as `pd`?'

def test_task2():
    assert type(pandas_101.wine) == type(wine), 'Have you loaded the CSV method with proper arguments and assigned to the variable wine?'

def test_task3():
    assert pandas_101.shape == (1599,12) , 'The loaded CSV should have 12 columns and 1599 rows. Use the shape function like so::shape=wine.shape'

def test_task4():
    assert pandas_101.chlorides.shape == chloride_test.shape, 'Have you selected all the rows of the chlorides column and named the variable chlorides?'

def test_task5():
    assert pandas_101.chlorides_mean == 0.08746654158849279, 'You can use the `wine.chlorides.mean()` call to calculate the correct mean. Assign answer to the variable chloride_mean'

def test_task6():
    assert os.path.exists('data/chlorides.csv'), 'did you save the chlorides series as  "chlorides.csv" to the data folder?'

