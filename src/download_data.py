#' Download data and save it 
#'
#' Download data from a source (either URL or relative local path) and save it locally to provided relative local path
#' 
#' @param source a source (either URL or relative local path) to download data from
#' @param path a local path/filename to write the file to and what to call it
#'
#' @return creates a file based off the dataset from 'source' and saves it at/as 'path'
#'
#' @export
#'
#' @examples
#' python ./src/download_data.py 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data' '../data/adult.data' 
import argparse
import shutil
import urllib3
import os

parser = argparse.ArgumentParser(description='Download data from a source (either URL or relative local path) and save it locally to provided relative local path')
parser.add_argument('source', metavar='source', type=str, help='a source (either URL or relative local path) to download data from')
parser.add_argument('path', metavar='path', type=str, help='a local path/filename to write the file to and what to call it')

args = parser.parse_args()
source = args.source
path = args.path

if (os.path.exists(source)):
    shutil.copyfile(source, path)
else:
    urllib3.request.urlretrieve(source,path)