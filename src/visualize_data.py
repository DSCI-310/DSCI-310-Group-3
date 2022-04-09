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
#' python ./src/visualize_data.py ./data/adult.data ./data/adult_data_plot.png age education-num
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from group3package.regression import regression

parser = argparse.ArgumentParser(description='Download data from a source (either URL or relative local path) and save it locally to provided relative local path')
parser.add_argument('source', metavar='source', type=str, help='a local path/filename pointing to the data')
parser.add_argument('path', metavar='path', type=str, help='a local path/filename prefix where to write the figure to and what to call it')
parser.add_argument('x', metavar='x', type=str, help="an explanatory numerical variable represented as a column's index in the 'source' data set")
parser.add_argument('y', metavar='y', type=str, help="a response numerical variable represented as a column's index in the 'source' data set")

args = parser.parse_args()
source = args.source
path = args.path
x = args.x
y = args.y

df = pd.read_csv(source)
x_col = df[x]
y_col = df[y]

m, b = regression(x_col, y_col)

plt.scatter(x_col, y_col, color = "#112E51")
plt.plot(x_col, m*x_col+b, color = "#FF7043")

plt.savefig(path)