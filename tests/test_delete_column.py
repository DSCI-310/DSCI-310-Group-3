import pytest
import pandas as pd
import numpy as np
import sys
sys.path.append(".")
from Python.remove_column import remove_column as rc

# assign data of lists.  
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
data_a = {'Name': ['Tom', 'Joseph', 'Krish', 'John']}
data_b = {'Age': [20, 21, 19, 18]}
  
# Create DataFrame
df = pd.DataFrame(data)
expected_a = pd.DataFrame(data_a)
expected_b = pd.DataFrame(data_b)

assert expected_a.equals(rc(df, 'Age'))
assert expected_b.equals(rc(df, 'Name'))
assert df.equals(rc(df, 'Does_not_exist'))

