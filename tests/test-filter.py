from pandas.testing import assert_frame_equal
import pandas as pd
from ..Python.filter import filter

df = pd.DataFrame({'a': ["Foo", "Bar"], 'b' : [1, 2]})
expected_a = pd.DataFrame({'a': ["Foo"], 'b' : [1]})
expected_b = pd.DataFrame({'a': ["Bar"], 'b' : [2]})

assert_frame_equal(expected_a, filter(df, "a", "Foo"))
assert_frame_equal(expected_b, filter(df, "b", 2))
