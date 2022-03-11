import pytest
import pandas as pd
import sys

sys.path.append(".")
from Python import filter as f

df = pd.DataFrame({'a': ["Foo", "Bar"], 'b' : [1, 2]})
expected = pd.DataFrame({'a': ["Foo"], 'b' : [1]})
assert expected.equals(f.filter(df, "a", "Foo"))

