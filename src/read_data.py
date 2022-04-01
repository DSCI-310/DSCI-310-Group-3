# add documentation 

import pandas as pd
from src.download_data import path
from src.remove_column import remove_column
import argparse
import sys

    
# load data, specifying there are no column names included in a header
#data = pd.read_csv(path, header=None)   ## Path should be the output of download_data script

parser = argparse.ArgumentParser(description='Reads and cleans data')
parser.add_argument('raw_data', metavar='source', type=str, help='a local path/filename pointing to the raw data')

parser.add_argument('clean_data', metavar='path', type=str, help='a local path/filename pointing to the clean data')

args = parser.parse_args()
raw_data = args.raw_data
clean_data = args.clean_data


df = pd.read_csv(raw_data, header=None)


def clean_data(df):
    names = ['age',
        'workclass',
        'fnlwgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'income']
    df.columns = names
    df = remove_column(raw_data, "race")
    df = remove_column(raw_data, "sex")
    return df

new_data = clean_data(df)
new_data.to_csv('clean_data')







### Old version:
# prepare column names
#names = ['age',
#        'workclass',
#        'fnlwgt',
#        'education',
#        'education-num',
#        'marital-status',
#        'occupation',
#        'relationship',
#        'race',
#        'sex',
#        'capital-gain',
#        'capital-loss',
#        'hours-per-week',
#        'native-country',
#        'income']

# assign column names
#data.columns = names

# drop some unused columns
#data = remove_column(data, "race")
#data = remove_column(data, "sex")

# view examples in dataset
#data.head()

