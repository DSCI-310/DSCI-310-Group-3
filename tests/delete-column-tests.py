from pandas.testing import assert_frame_equal
import pandas as pd
from ..Python.remove_column import remove_column

# assign data of lists.  
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
data_a = {'Name': ['Tom', 'Joseph', 'Krish', 'John']}
data_b = {'Age': [20, 21, 19, 18]}
  
# Create DataFrame
df = pd.DataFrame(data)
expected_a = pd.DataFrame(data_a)
expected_b = pd.DataFrame(data_b)

assert data_a == data.remove_column(data, 'Age')
assert data_b == data.remove_column(data, 'Name')

