import numpy as np
import pandas as pd

#remove rows in the data frame with nulls above the threshold
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
def fillColsWithMedian(dataframe, stat):
    median = findMedianOfCol(dataframe, stat)
    dataframe = dataframe.fillna(median)
    return dataframe

#fill all columns with the mean of the column
def fillColsWithMean(dataframe,stat):
    mean = findMeanOfCol(dataframe,stat)
    dataframe = dataframe.fillna(mean)
    return dataframe


# find median of a column
def findMedianOfCol(dataframe, colName):
    median = dataframe[colName].median()
    return median


# find the mean of a column
def findMeanOfCol(dataframe, colName):
    mean = dataframe[colName].mean()
    return mean

def mergeAllFrames(dataFrames):
    while len(dataFrames > 1):
        for i in range(len(dataFrames), 2):
            dataFrames[i] = mergeFrames(dataFrames[i], dataFrames[(i + 1)], 'year')
    return dataFrames

def mergeFrames(frame1, frame2,on):
    mergedFrames = pd.merge(frame1,frame2, on = [on], how ='outer')
    return mergedFrames



#converts and array in the form ['yyyy-mm-dd','YYYY-MM-DD'] to an array into the form (int)[yyyy,YYYY]
def convertDateStringToInt(dateRange):
    start = dateRange[0]
    start = start[0:4] #selecting only the first 4 characters which correspond to the year
    start = int(start) #converting from a string to an int to match df's year_ID data type

    #Determine the end of the required time period
    end = dateRange[1]
    end = end[0:4]
    end = int(end)
    array = [start,end]
    return array


def perGameConversionAll(dataframe,team):
    columns = dataframe.columns.values
    print(columns)
    for x in columns:
        print(x)
        if (type(dataframe[x].values[0]) != str):
                if(team==0):
                    if (x != 'G'):
                         dataframe[x] = dataframe[x] / dataframe['G']
                elif(team ==1):
                    if(x!='GS'):
                        dataframe[x] = dataframe[x]/162 #mlb seasons have been 162 games long for decades.
                    # The line above  could be changed to dataframe[x] = dataframe[x]/dataframe['GS'], but the user would have to remember to include the GS column
                else:
                    print("error, please enter if the dataframe contains team stats or individual stats")
    return dataframe


# stats is an array of columns would be converted to per game
def perGameConversion(dataframe,stats,team):
    for x in stats:
        if (type(dataframe[x].values[0]) != str):
                if(team==0):
                    if (x != 'G'):
                         dataframe[x] = dataframe[x] / dataframe['G']
                elif(team ==1):
                    if(x!='GS'):
                         dataframe[x] = dataframe[x]/162 #mlb seasons have been 162 games long for decades.
                    # The line above  could be changed to dataframe[x] = dataframe[x]/dataframe['GS'], but the user would have to remember to include the GS column
                else:
                    print("error, please enter if the dataframe contains team stats or individual stats")
    return dataframe




