import pytest
import pandas as pd
import numpy as np
import sys
sys.path.append(".")
from src.remove_column import remove_column as rc

#test the remove_column function in the remove_column.py file

# assign data of lists.  
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
data_a = {'Name': ['Tom', 'Joseph', 'Krish', 'John']}
data_b = {'Age': [20, 21, 19, 18]}
  
# Create DataFrame
df = pd.DataFrame(data)
expected_a = pd.DataFrame(data_a)
expected_b = pd.DataFrame(data_b)

#Expect the Age column to be removed from the data frame
assert expected_a.equals(rc(df, 'Age')) 

#Expect the Name column to be removed from the data frame
assert expected_b.equals(rc(df, 'Name'))

#Test for wrong input into the function should produce the same data frame as before (no column is removed)
assert df.equals(rc(df, 'Does_not_exist'))

