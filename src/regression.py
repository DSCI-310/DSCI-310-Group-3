#' Performs linear regression on data and returns variables found
#'
#' Calls numpy's polyfit function with a degree of 1
#' 
#' @param x a vector to use as the x axis in the regression
#' @param y a vector to use as the y axis in the regression
#'
#' @return parameters m and b in the line of best fit y=m*x+b
#'
#' @export
#'
#' @examples
#' m, b = regression(x, y)

from numpy import polyfit

def regression(x, y):
    m, b = polyfit(x, y, 1)
    
    return m, b