#' read data, clean it and save it as a new csv
#'
#' Download data from local path, perform cleaning on it, and save it locally to provided relative local path
#' 
#' @param raw-data a local path to read data from
#' @param clean-data a local path/filename to save clean data as csv file


import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Makes summary table')
parser.add_argument('data', metavar='source', type=str, help='a local path/filename pointing to the data')

parser.add_argument('chart', metavar='path', type=str, help='a local path/filename pointing to the the chart')

args = parser.parse_args()
data = args.data
chart = args.chart

df = pd.read_csv(data, header=None)

data = {'Number of observations': [len(df.index)],
        'average education':  [df["education-num"].mean()],
        'average hours worked': [df["hours-per-week"].mean()],
        'average capital gain': [df["capital-gain"].mean()]
        }

new_df = pd.DataFrame(data)

new_df.to_csv('chart')


#import pandas as pd
#from src.remove_column import remove_column
#import argparse

#parser = argparse.ArgumentParser(description='Reads and cleans data')
#parser.add_argument('raw_data', metavar='source', type=str, help='a local path/filename pointing to the raw data')

#parser.add_argument('clean_data', metavar='path', type=str, help='a local path/filename pointing to the clean data')

#args = parser.parse_args()
#raw_data = args.raw_data
#clean_data = args.clean_data


#df = pd.read_csv(raw_data, header=None)


#def clean_data(df):
#    names = ['age',
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
#    df.columns = names
#    df = remove_column(raw_data, "race")
#    df = remove_column(raw_data, "sex")
#    return df

#new_data = clean_data(df)
#new_data.to_csv('clean_data')








