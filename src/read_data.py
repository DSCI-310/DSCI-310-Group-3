# add documentation 

import pandas as pd
from src.download_data import path
from src.remove_column import remove_column

    
# load data, specifying there are no column names included in a header
#data = pd.read_csv(path, header=None)   ## Path should be the output of download_data script

def read_clean_data(data_path): #param should be from downlaod_data script
    data_path = path #should this be added?
    raw_data = pd.read_csv(data_path, header=None)
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
    raw_data.columns = names
    raw_data = remove_column(raw_data, "race")
    raw_data = remove_column(raw_data, "sex")
    return raw_data.head()

