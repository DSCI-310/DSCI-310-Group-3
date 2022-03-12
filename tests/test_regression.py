import pytest
import numpy as np
import pandas as pd
import sys
sys.path.append(".")
from Python.regression import regression

x = [1,2]
y = [2,4]
results = pd.DataFrame(regression(x,y))

# note: regression gives the following values, not exactly '2' and '0'
expected_m = 1.9999999999999991
expected_b = 1.25607396694702e-15
expected = pd.DataFrame([expected_m, expected_b])

assert expected.equals(results)


def testLinAlgError():
    with pytest.raises(Exception):
        results = regression([0,0],[0,0])