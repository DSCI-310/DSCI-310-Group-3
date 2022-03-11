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
def remove_column(df, column_name):
  #return new data frame with removed columns 
