#' read data, clean it and save it as a new csv
#'
#' Download data from local path, perform cleaning on it, and save it locally to provided relative local path
#' 
#' @param raw-data a local path to read data from
#' @param clean-data a local path/filename to save clean data as csv file
#' @export
#'
#' @examples
#' python ./src/process_data.py "data/adult.data" "./data/graph.data" 


import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Makes summary table')
parser.add_argument('data', metavar='source', type=str, help='a local path/filename pointing to the data')

parser.add_argument('chart', metavar='path', type=str, help='a local path/filename pointing to the the chart')

args = parser.parse_args()
data = args.data
chart = args.chart

df = pd.read_csv(data, header=None)

data = [['Number of observations', [len(df.index)]],
        ['average education',  [df["education-num"].mean()]],
        ['average hours worked', [df["hours-per-week"].mean()]],
        ['average capital gain', [df["capital-gain"].mean()]]]

new_df = pd.DataFrame(data)

new_df.to_csv('chart')














