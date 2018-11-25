'''
bWarPitch  is a function that takes in 4 parameters and returns a pd data frame
1. mld_ID is an array of integers of the the mld_ID that corresponds to the required player(s)
2. stats is the kind of data that is required in the form of an array of strings
3. range is an array of two strings in the form [yyyy-mm-dd,yyy-mm-dd] which indicates the time period of the required data
'''

from pybaseball import bwar_pitch
import pandas as pd

def bWarPitch(mlb_ID,stats,range):


    #Select the correct version of bwar_pitch
    data = bwar_pitch(return_all=1)

    #Create a panda data frame from the data
    df = pd.DataFrame(data)

    #eliminate by mlb_ID
    df = df[df.mlb_ID.isin(mlb_ID)]

    #eliminate by stats
    df = df.filter(items=stats)

    #Note: bwar_pitch only contain time periods by the year
    #Determine the start of the required time period
    start = range[0]
    start = start[0:4] #selecting only the first 4 characters which correspond to the year
    start = int(start) #converting from a string to an int to match df's year_ID data type

    #Determine the end of the required time period
    end = range[1]
    end = end[0:4]
    end = int(end)

    #eliminate by year
    df = df[(df.year_ID >= start) & (df.year_ID <= end)]

    return df
