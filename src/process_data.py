#' Format dataframe and save it 
#'
#' Assign column names and remove unused columns, then resave as a new csv, renaming the old data csv instead of deleting
#' 
#' @param source the local path of the downloaded data csv
#'
#' @return renames original csv by adding '_unprocessed.data' to it and replaces original with a processed version
#'
#' @export
#'
#' @examples
#' python ./src/process_data.py "data/adult.data" 
import argparse
import os
import pandas as pd

import sys
sys.path.append("..")
from remove_column import remove_column

parser = argparse.ArgumentParser(description='Load data from provided path and process it for analysis')
parser.add_argument('source', metavar='source', type=str, help='path to downloaded data')

args = parser.parse_args()
source = args.source

if (os.path.exists(source)):
    
    # load data, specifying there are no column names included in a header
    data = pd.read_csv(source, header=None)
    
    # save a copy of it at the new location
    new = source + '_unprocessed.data'
    data.to_csv(new, index = None, header=False)
    
    # prepare column names
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

    # assign column names
    data.columns = names

    # drop some unused columns
    data = remove_column(data, "race")
    data = remove_column(data, "sex")

    
    # save processed data
    data.to_csv(source, index = None, header=True)
    
else:
    print("Data not found")
    print(source)
    print(os.getcwd())