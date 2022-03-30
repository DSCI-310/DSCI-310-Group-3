#' Create exploratory data visualizations/tables
#'
#' Creates exploratory data visualizations and tables to help reader/consumers understand dataset
#' 
#' @param source a local path/filename pointing to a csv
#' @param path a local path/filename prefix where to write the figure to and what to call it
#' @param x an explanatory numerical variable represented as a column's index in the 'source' data set
#' @param y a response numerical variable represented as a column's index in the 'source' data set
#'
#' @return a scatter plot with a regression line that represents the given explantory and response variables
#'
#' @export
#'
#' @examples
#' python ./src/visualize_data.py './data/adult.data' './data/adult_data_plot.csv' '0' '2' 
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from regression import regression

parser = argparse.ArgumentParser(description='Download data from a source (either URL or relative local path) and save it locally to provided relative local path')
parser.add_argument('source', metavar='source', type=str, help='a local path/filename pointing to the data')
parser.add_argument('path', metavar='path', type=str, help='a local path/filename prefix where to write the figure to and what to call it')
parser.add_argument('x', metavar='x', type=int, help="an explanatory numerical variable represented as a column's index in the 'source' data set")
parser.add_argument('y', metavar='y', type=int, help="a response numerical variable represented as a column's index in the 'source' data set")

args = parser.parse_args()
source = args.source
path = args.path
x = args.x
y = args.y

df = pd.read_csv(source, header=None)
x_col = df.iloc[:, x]
y_col = df.iloc[:, y]

m, b = regression(x_col, y_col)

plt.scatter(x_col, y_col)
plt.plot(x_col, m*x_col+b)

# TODO: save to path