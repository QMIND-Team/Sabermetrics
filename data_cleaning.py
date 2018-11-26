import numpy as np
import pandas as pd

# gets dataframe, calls cleaning functions, returns clean data
# Mike
def cleaning(dataframe, nullThreshRow, nullThreshCol):
   return 0

#remove rows in the data frame with nulls above the threshold
#Eric
def removeNullThreshRows(dataframe, nullThreshRow):
     length = dataframe.shape[1]
     dataframe = dataframe.dropna(axis=0,thresh=length-nullThreshRow)
     return dataframe

# remove columns in the data frame with nulls above the threshold
def removeNullThreshColumns(dataframe, nullThreshCol):
     length = dataframe.shape[0]
     dataframe = dataframe.dropna(axis=1,thresh=length-nullThreshCol)
     return dataframe

# count number of nulls in each row
# Vedant
def countRowNulls(dataframe):
    '''
    Index can be given to get number of null columns in a particular row.
    :param dataframe: pandas DataFrame
    :return: pandas Series: number of null values in each row
    '''
    return dataframe.isna().sum(axis=1)

# count number of nulls in each column
def countColumnNulls(dataframe):
    '''
    :param dataframe: pandas DataFrame
    :return: pandas Series: number of null values within each column
    '''
    return dataframe.isna().sum()

# fill a column with the median of the column
# Will
def fillColsWithMedian(dataframe, colNum):
    median = findMedianOfCol(dataframe, colNum)
    dataframe.iloc[:, colNum] = dataframe.iloc[:, colNum].fillna(median)
    return dataframe

# fill a column with the mean of the column
def fillColsWithMean(dataframe, colNum):
    mean = findMeanOfCol(dataframe, colNum)
    dataframe.iloc[:, colNum] = dataframe.iloc[:, colNum].fillna(mean)
    return dataframe

# find the median of a column
def findMedianOfCol(dataframe, colNum):
    return 0

# find the mean of a column
def findMeanOfCol(dataframe, colNum):
    return 0
