import pybaseball as bball
import pandas as pd
import numpy as np
import modules.data_processing.data_cleaning as dc

# Mike
def query(source, stats, dateRange, league='None', aggregate='None', pitcherId='None'):

    if source == "fangraphs":
        dataframe = pitchingFangraphsData(dateRange, stats)
    elif source == "bref":
        dataframe = pitchingBrefData(dateRange, stats)
    elif source == "savant":
        dataframe = pitchingBaseballSavantData(dateRange, stats)
    elif source == "teamPitching":
        dataframe = teamPitchingData(dateRange, stats, league, aggregate)
    elif source == "bWar":
        dataframe = bWarData(dateRange, stats)
    elif source == "statcast":
        dataframe = statcastData(pitcherId, stats, dateRange)
    else:
        # TODO
        raise Exception

    return dataframe

def statcastData(pitcherId, stats, dateRange):
    if pitcherId is None:
        # TODO
        raise Exception

    data = bball.statcast_pitcher(dateRange[0], dateRange[1], pitcherId)
    statcastDF = pd.DataFrame(data)
    statsOnly = statcastDF[stats]
    return statsOnly

def teamPitchingData(dateRange, stats, league, aggregate):
    if league is None or aggregate is None:
        # TODO
        raise Exception

    period = dc.convertDateStringToInt(dateRange)

    # new
    data = pd.read_csv("../csv/team_pitching.csv", index_col=0)
    df = pd.DataFrame()
    for i in range(period[0], period[1] + 1):
        # print(i)
        # print(data[data["Season"] == i])
        df = pd.concat([df, data[data["Season"] == i]])
    # df = bball.team_pitching(period[0], period[1], league, aggregate)

    # ignore the parameters like player_id
    # drop all columns from the dataframe except the ones specified in stats
    dfHeaders = list(df.columns)
    neededCols = stats + ['Team', 'Season']
    dropCols = []
    for column in dfHeaders:
        if column not in neededCols:
            dropCols += [column]
    df = df.drop(dropCols, axis = 1)
    return df

def teamPitching(start, end=None):
    if end is None:
        end = start
    data = pd.read_csv("../csv/team_pitching.csv", index_col=0)
    df = pd.DataFrame()
    for i in range(start, end + 1):
        # print(i)
        # print(data[data["Season"] == i])
        df = pd.concat([df, data[data["Season"] == i]])
    # df = bball.team_pitching(period[0], period[1], league, aggregate)

    # ignore the parameters like player_id
    # drop all columns from the dataframe except the ones specified in stats

    # dfHeaders = list(df.columns)
    # neededCols = stats + ['Team', 'Season']
    # dropCols = []
    # for column in dfHeaders:
    #     if column not in neededCols:
    #         dropCols += [column]
    # df = df.drop(dropCols, axis = 1)

    return df

def teamBattingData(dateRange, stats, league, aggregate):
    if league is None or aggregate is None:
        # TODO
        raise Exception

    period = dc.convertDateStringToInt(dateRange)

    # new
    data = pd.read_csv("../csv/team_batting.csv", index_col=0)
    df = pd.DataFrame()
    for i in range(period[0], period[1] + 1):
        # print(i)
        # print(data[data["Season"] == i])
        df = pd.concat([df, data[data["Season"] == i]])
    # df = bball.team_pitching(period[0], period[1], league, aggregate)

    # ignore the parameters like player_id
    # drop all columns from the dataframe except the ones specified in stats
    dfHeaders = list(df.columns)
    neededCols = stats + ['Team', 'Season']
    dropCols = []
    for column in dfHeaders:
        if column not in neededCols:
            dropCols += [column]
    df = df.drop(dropCols, axis = 1)
    return df

def teamBatting(start, end=None):
    if end is None:
        end = start
    data = pd.read_csv("../csv/team_batting.csv", index_col=0)
    df = pd.DataFrame()
    for i in range(start, end + 1):
        # print(i)
        # print(data[data["Season"] == i])
        df = pd.concat([df, data[data["Season"] == i]])
    # df = bball.team_pitching(period[0], period[1], league, aggregate)

    # ignore the parameters like player_id
    # drop all columns from the dataframe except the ones specified in stats

    # dfHeaders = list(df.columns)
    # neededCols = stats + ['Team', 'Season']
    # dropCols = []
    # for column in dfHeaders:
    #     if column not in neededCols:
    #         dropCols += [column]
    # df = df.drop(dropCols, axis = 1)

    return df

# bWarPitch  is a function that takes in 4 parameters and returns a pd data frame
# 1. mld_ID is an array of integers of the the mld_ID that corresponds to the required player(s)
# 2. stats is the kind of data that is required in the form of an array of strings
# 3. range is an array of two strings in the form [yyyy-mm-dd,yyy-mm-dd] which indicates the time period of the required data
def bWarData(dateRange, stats):
    #Select the correct version of bwar_pitch
    df = pd.read_csv("../csv/bwar.csv", index_col=0)

    #Create a panda data frame from the data
    #df = pd.DataFrame(data)

    #eliminate by stats
    df = df.filter(items=stats)

    period = dc.convertDateStringToInt(dateRange)

    #eliminate by year
    df = df[(df.year_ID >= period[0]) & (df.year_ID <= period[1])]
    return df

def pitchingFangraphsData(dateRange, stats):
    # extracting year from start date
    startStr = dateRange[0]
    start = int(startStr[:4])

    # extracting year from end date
    endStr = dateRange[1]
    end = int(endStr[:4])

    # get pitching_stats for specific range given
    print("Gathering Data from Fangraphs")
    pitchStats = pd.DataFrame()
    df = pd.read_csv('../csv/pitching_fangraphs.csv')
    for i in range(start, end + 1):
        pitchStats.concat([pitchStats, df[df['Season'] == i]])
    print("Data Gathering Complete")
    pitchStatsDF = pd.DataFrame(pitchStats)
    headersList = pitchStatsDF.columns
    headers = np.asarray(headersList)

    # drop columns that are in the input stats array
    keepStats = []
    index = []
    count = 0
    for i in stats:
        for j in headers:
            if j == i:
                index.insert(len(index) + 1, count)
                keepStats.insert(len(keepStats) + 1, j)
            count = count + 1
        count = 0

    dropCols = np.delete(headers, index)
    drop = np.asarray(dropCols)

    # drop the columns from pitching stats with these names
    pitchStatsDF = pitchStatsDF.drop(columns=drop)
    return pitchStatsDF

def pitchingBrefData(dateRange, stats):
    # extracting year from start date
    startStr = dateRange[0]
    start = startStr[:4]

    # extracting year from end date
    endStr = dateRange[1]
    end = endStr[:4]

    # make bounds based on start and end dates
    a = int(start)
    b = int(end)
    '''
    finalStats = pd.DataFrame()

    # loop to get data from every year
    while a <= b:
        # make a Data Frame for the specific year and take a list of headers
        pitchStats = bball.pitching_stats_bref(a)
        pitchStatsDF = pd.DataFrame(pitchStats)
        pitchStatsDF['Year'] = a

        # appending to one single Data Frame
        finalStats = finalStats.append(pitchStatsDF)

        # go to next year
        a = a + 1
    '''
    data = pd.read_csv("../csv/pitching_stats_bref.csv", index_col=0)
    finalStats = pd.DataFrame()
    for i in range(a, b + 1):
        # print(i)
        # print(data[data["Season"] == i])
        finalStats = pd.concat([finalStats, data[data["Year"] == i]])

    finalStats = finalStats[stats]
    return finalStats

def battingBrefData(dateRange, stats):
    # extracting year from start date
    startStr = dateRange[0]
    start = startStr[:4]

    # extracting year from end date
    endStr = dateRange[1]
    end = endStr[:4]

    # make bounds based on start and end dates
    a = int(start)
    b = int(end)
    '''
    finalStats = pd.DataFrame()

    # loop to get data from every year
    while a <= b:
        # make a Data Frame for the specific year and take a list of headers
        pitchStats = bball.pitching_stats_bref(a)
        pitchStatsDF = pd.DataFrame(pitchStats)
        pitchStatsDF['Year'] = a

        # appending to one single Data Frame
        finalStats = finalStats.append(pitchStatsDF)

        # go to next year
        a = a + 1
    '''
    data = pd.read_csv("../csv/batting_stats_bref.csv", index_col=0)
    finalStats = pd.DataFrame()
    for i in range(a, b + 1):
        # print(i)
        # print(data[data["Season"] == i])
        finalStats = pd.concat([finalStats, data[data["Year"] == i]])

    finalStats = finalStats[stats]
    return finalStats

def pitchingBref(start, end=None):
    if end is None:
        end = start
    data = pd.read_csv("../csv/pitching_stats_bref.csv", index_col=0)
    finalStats = pd.DataFrame()
    for i in range(start, end + 1):
        # print(i)
        # print(data[data["Season"] == i])
        finalStats = pd.concat([finalStats, data[data["Year"] == i]])

    return finalStats

def battingBref(start, end=None):
    if end is None:
        end = start
    data = pd.read_csv("../csv/batting_stats_bref.csv", index_col=0)
    finalStats = pd.DataFrame()
    for i in range(start, end + 1):
        # print(i)
        # print(data[data["Season"] == i])
        finalStats = pd.concat([finalStats, data[data["Year"] == i]])

    return finalStats

def pitchingBaseballSavantData(dateRange, stats):
    # get pitching_stats for specific range given
    pitchStats = bball.pitching_stats_range(dateRange[0], dateRange[1])
    pitchStatsDF = pd.DataFrame(pitchStats)
    headersList = pitchStatsDF.columns
    headers = np.asarray(headersList)

    # drop columns that are in the input stats array
    keepStats = []
    index = []
    count = 0
    for i in stats:
        for j in headers:
            if j == i:
                index.insert(len(index) + 1, count)
                keepStats.insert(len(keepStats) + 1, j)
            count = count + 1
        count = 0

    dropCols = np.delete(headers, index)
    drop = np.asarray(dropCols)

    # drop the columns from pitching stats with these names
    pitchStatsDF = pitchStatsDF.drop(columns=drop)
    return pitchStatsDF
