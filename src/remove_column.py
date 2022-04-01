#' Remove columns in data set
#'
#' Removes the column the function takes as a parameter
#' from the data set
#'
#' @param data_frame A data frame or data frame extension (e.g. a tibble).
#' @param column_name quoted column name of column containing data that should be removed
#'
#' @return A data frame without the data that was suppose to be removed. 
#'   Should have at least one less column when the function is called
#'
#' @export
#'
#' @examples
#' remove_column(df, df_column_name)

from pandas import DataFrame as DF

def remove_column(df, column_name):
    
    if type(df) != DF:
        raise Exception("Expected DataFrame, got", type(df))
    
    if column_name in df.columns:
        return df.drop(column_name, 1, inplace=False)
    else:
        return df
