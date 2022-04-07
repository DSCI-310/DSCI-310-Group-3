import pytest
import pandas as pd
import numpy as np
import sys

sys.path.append(".")
from src.filter import filter as f

df = pd.DataFrame({'a': ["Foo", "Bar"], 'b' : [1, 2]})
expected = pd.DataFrame({'a': ["Foo"], 'b' : [1]})

# Testing if filter can extract a row given an existing column and value in dataframe
def test_basic_filter():
    assert expected.equals(f(df, "a", "Foo")), "Correct dataframe was not correctly filtered."

# Testing if filter returns empty dataframe when given an existing column and non-existent value
def test_non_existent_value():
    assert f(df, "a", "NonExistent").empty, "Dataframe is not empty."

# Testing if filter throws an error when given a non-existent column
def test_non_existent_column():
    with pytest.raises(KeyError) as exc_info:
        f(df, "c", "Foo").empty
    assert exc_info.type is KeyError, "Exception was not thrown"

# Testing if filter throws an error when given a non-existent dataframe
def test_non_existent_dataframe():
    with pytest.raises(NameError) as exc_info:
        f(data, "a", "Foo").empty
    assert exc_info.type is NameError, "Exception was not thrown"