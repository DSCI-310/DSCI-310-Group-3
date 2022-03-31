import pytest
import numpy as np
import pandas as pd
import sys
sys.path.append(".")
from src.regression import regression

x = [1,2]
y = [2,4]
results = pd.DataFrame(regression(x,y)).round(decimals=0)

# note: regression gives the following values, not exactly '2' and '0'
expected_m = 2.0
expected_b = 0.0
expected = pd.DataFrame([expected_m, expected_b])

assert expected.equals(results)


def testLinAlgError():
    with pytest.raises(Exception):
        results = regression([0,0],[0,0])