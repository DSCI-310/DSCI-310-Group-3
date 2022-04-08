import pytest
import numpy as np
import pandas as pd
import sys
sys.path.append(".")
from src.regression import regression

# setup sample data
x = [1,2]
y = [2,4]
# run regression, round to avoid OS-based discrepancies, and wrap in DataFrame
results = pd.DataFrame(regression(x,y)).round(decimals=0)

# compare regression with expected values, also in DataFrame for easy comparison
expected_m = 2.0
expected_b = 0.0
expected = pd.DataFrame([expected_m, expected_b])

# test that we get the expected values
assert expected.equals(results), "Regression function did not return correct results"

# a simple test to ensure we cannot run regression on all zeros
def testLinAlgError():
    with pytest.raises(Exception):
        results = regression([0,0],[0,0])