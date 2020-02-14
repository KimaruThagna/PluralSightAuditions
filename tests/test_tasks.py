import pytest, os
from .utils import get_calls, get_assignments
import pandas_101


@pytest.mark.test_task1
def test_task1():
    assert 'pd' in dir(pandas_101), 'Have you imported the`pandas` library with an alias as `pd`?'

@pytest.mark.test_task2
def test_task2():
    assert get_calls(pandas_101)[0] == 'data/winequality-red.csv', 'Have you loaded the CSV file using the `pd.read_csv()` method with proper arguments?'
    assert get_assignments(pandas_101)[0][:2] == 'wine', 'Has the `wine` DataFrame been created?'

@pytest.mark.test_task3
def test_task3():
    assert get_assignments(pandas_101)[1][:12] == 'shape', 'Has the `shape` variable been created?'
    assert pandas_101.shape == () , 'The loaded CSV should have _ columns and _ rows'

@pytest.mark.test_task4
def test_task4():
    assert get_assignments(pandas_101)[1][:12] == 'chlorides', 'Has the `chlorides` variable been created?'

@pytest.mark.test_task5
def test_task5():
    assert os.path.exists('data/new_csv.csv'), 'Was the new_csv.csv file created in the data folder?'

@pytest.mark.test_task6
def test_task6():
    assert pandas_101.chlorides_mean == 7.25, 'You can use the `wine.chlorides.mean()` call to calculate the correct mean.'