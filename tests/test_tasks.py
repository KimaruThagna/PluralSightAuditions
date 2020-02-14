import pytest
from .utils import get_calls, get_assignments
import pandas_101


@pytest.mark.test_task1
def test_task1():
    assert 'pd' in dir(pandas_101), 'Have you imported the`pandas` library with an alias as `pd`?'
    assert 'np' in dir(pandas_101), 'Have you imported the`numpy` library with an alias as `np`?'



@pytest.mark.test_task2
def test_task2():
    assert get_calls(pandas_101)[0] == 'pd:read_csv:data/data/winequality-red.csv', 'Have you loaded the CSV file using the `pd.read_csv()` method with proper arguments?'
    assert get_assignments(pandas_101)[0][:2] == 'df', 'Has the `df` DataFrame been created?'


@pytest.mark.test_task3
def test_task3():
    assert get_assignments(pandas_101)[1][:12] == 'grade_median', 'Has the `grade_median` variable been created?'
    assert pandas_101.grade_median == 7.25, 'You can use the `df.GRADE.median()` call to calculate the correct median.'