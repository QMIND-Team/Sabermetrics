import numpy as np
import pandas as pd

#remove rows in the data frame with nulls above the threshold
def removeNullThreshRows(df, nullThreshRow):
     length = df.shape[1]
     df= df.dropna(axis=0,thresh=length-nullThreshRow)
     return df

# remove columns in the data frame with nulls above the threshold
def removeNullThreshColumns(df, nullThreshCol):
     length = df.shape[0]
     df = df.dropna(axis=1,thresh=length-nullThreshCol)
     return df

# count number of nulls in each row
# Vedant
def countRowNulls(df):
    '''
    Index can be given to get number of null columns in a particular row.
    :param df: pandas DataFrame
    :return: pandas Series: number of null values in each row
    '''
    return df.isna().sum(axis=1)

# count number of nulls in each column
def countColumnNulls(df):
    '''
    :param df: pandas DataFrame
    :return: pandas Series: number of null values within each column
    '''
    return df.isna().sum()

# fill a column with the median of the column
def fillColsWithMedian(df, stat):
    median = findMedianOfCol(df, stat)
    df = df.fillna(median)
    return df


#fill all columns with the mean of the column
def fillColsWithMean(df,stat):
    mean = findMeanOfCol(df,stat)
    df = df.fillna(mean)
    return df


# find median of a column
def findMedianOfCol(df, colName):
    median = df[colName].median()
    return median

# find the mean of a column
def findMeanOfCol(df, colName):
    mean = df[colName].mean()
    return mean

def mergeAllFrames(dfList):
    while len(dfList > 1):
        for i in range(len(dfList), 2):
            dfList[i] = mergeFrames(dfList[i], dfList[(i + 1)], 'year')
    return dfList

def mergeFrames(frame1, frame2,on):
    mergedFrames = pd.merge(frame1,frame2, on = on, how ='inner')
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

def perGameConversionAll(df, team):
    columns = df.columns.values
    print(columns)
    for x in columns:
        print(x)
        if (type(df[x].values[0]) != str):
                if(team==0):
                    if (x != 'G'):
                         df[x] = df[x] / df['G']
                elif(team ==1):
                    if(x!='GS'):
                        df[x] = df[x]/162 #mlb seasons have been 162 games long for decades.
                    # The line above  could be changed to df[x] = df[x]/df['GS'], but the user would have to remember to include the GS column
                else:
                    print("error, please enter if the df contains team stats or individual stats")
    return df

# stats is an array of columns would be converted to per game
def perGameConversion(df,stats,team):
    for x in stats:
        if (type(df[x].values[0]) != str):
                if(team==0):
                    if (x != 'G'):
                         df[x] = df[x] / df['G']
                elif(team ==1):
                    if(x!='GS'):
                         df[x] = df[x]/162 #mlb seasons have been 162 games long for decades.
                    # The line above  could be changed to df[x] = df[x]/df['GS'], but the user would have to remember to include the GS column
                else:
                    print("error, please enter if the dataframe contains team stats or individual stats")
    return df
