import pybaseball as bball
import pandas as pd

# Mike
def query(pitcherId, stats, dateRange, league, aggregate):
    statsType = checkStatsFiles(stats)

# Mike
def checkStatsFiles(stats):
    statsToUse = None
    return(statsToUse)

def statcastData(pitcherId, stats, dateRange):
    statcastData = bball.statcast_pitcher(dateRange[0], dateRange[1], pitcherId)
    statcastDF = pd.DataFrame(statcastDF)
    statsOnly = statcastDF[stats]
    return(statsOnly)

def teamPitchingData(teamName, dateRange, stats, league, aggregate):
    df = bball.team_pitching(dateRange[0], dateRange[1], league, aggregate)

    # ignore the parameters like player_id

    # drop all columns from the dataframe except the ones specified in stats
    df_headers = list(df.columns)
    needed_cols = stats + ['Team', 'Season']
    drop_cols = []
    for col in df_headers:
        if col not in needed_cols:
            drop_cols += [col]
    df = df.drop(drop_cols, axis = 1)
    return(df)

# bWarPitch  is a function that takes in 4 parameters and returns a pd data frame
# 1. mld_ID is an array of integers of the the mld_ID that corresponds to the required player(s)
# 2. stats is the kind of data that is required in the form of an array of strings
# 3. range is an array of two strings in the form [yyyy-mm-dd,yyy-mm-dd] which indicates the time period of the required data
def bWarData(pitcherId, dateRange, stats):
    #Select the correct version of bwar_pitch
    data = bwar_pitch(return_all=1)

    #Create a panda data frame from the data
    df = pd.DataFrame(data)

    #eliminate by mlb_ID
    df = df[df.pitcherId.isin(mlb_ID)]

    #eliminate by stats
    df = df.filter(items=stats)

    #Note: bwar_pitch only contain time periods by the year
    #Determine the start of the required time period
    start = dateRange[0]
    start = start[0:4] #selecting only the first 4 characters which correspond to the year
    start = int(start) #converting from a string to an int to match df's year_ID data type

    #Determine the end of the required time period
    end = dateRange[1]
    end = end[0:4]
    end = int(end)

    #eliminate by year
    df = df[(df.year_ID >= start) & (df.year_ID <= end)]
    return(df)

def pitchingFangraphsData(dateRange, stats):
    # extracting year from start date
    start_str = dateRange[0]
    start = start_str[:4]

    # extracting year from end date
    end_str = dateRange[1]
    end = end_str[:4]

    # get pitching_stats for specific range given
    pitch_stats = pitching_stats(start, end)
    pitch_stats_df = pd.DataFrame(pitch_stats)
    headersList = pitch_stats_df.columns
    headers = np.asarray(headersList)

    # drop columns that are in the input stats array
    keep_stats = []
    index = []
    count = 0
    for i in stats:
        for j in headers:
            if j == i:
                index.insert(len(index) + 1, count)
                keep_stats.insert(len(keep_stats) + 1, j)
            count = count + 1
        count = 0

    drop_cols = np.delete(headers, index)
    drop = np.asarray(drop_cols)

    # drop the columns from pitching stats with these names
    pitch_stats_df = pitch_stats_df.drop(columns=drop)
    return pitch_stats_df

def pitchingBrefData(dateRange, stats):
    # extracting year from start date
    start_str = dateRange[0]
    start = start_str[:4]

    # extracting year from end date
    end_str = dateRange[1]
    end = end_str[:4]

    # make bounds based on start and end dates
    a = int(start)
    b = int(end)

    # loop to get data from every year
    headers = []
    while a <= b:
        # make a Data Frame for the specific year and take a list of headers
        pitch_stats = pitching_stats_bref(a)
        pitch_stats_df = pd.DataFrame(pitch_stats)
        headersList = pitch_stats_df.columns
        headers = np.asarray(headersList)

        # drop columns that are in the input stats array
        keep_stats = []
        index = []
        count = 0
        for i in stats:
            for j in headers:
                if j == i:
                    index.insert(len(index) + 1, count)
                    keep_stats.insert(len(keep_stats) + 1, j)
                count = count + 1
            count = 0

        # make a list of columns that will be dropped
        drop_cols = np.delete(headers, index)
        drop = np.asarray(drop_cols)

        # drop the columns from pitching stats with these names
        pitch_stats_df = pitch_stats_df.drop(columns=drop)

        # appending to one single Data Frame
        pitch_stats_df.append(pitch_stats_df)

        # go to next year
        a = a + 1

        return pitch_stats_df

def pitchingBaseballSavantData(dateRange, stats):
    # get pitching_stats for specific range given
    pitch_stats = pitching_stats_range(dateRange[0], dateRange[1])
    pitch_stats_df = pd.DataFrame(pitch_stats)
    headersList = pitch_stats_df.columns
    headers = np.asarray(headersList)

    # drop columns that are in the input stats array
    keep_stats = []
    index = []
    count = 0
    for i in stats:
        for j in headers:
            if j == i:
                index.insert(len(index) + 1, count)
                keep_stats.insert(len(keep_stats) + 1, j)
            count = count + 1
        count = 0

    drop_cols = np.delete(headers, index)
    drop = np.asarray(drop_cols)

    # drop the columns from pitching stats with these names
    pitch_stats_df = pitch_stats_df.drop(columns=drop)
    return pitch_stats_df

# Eric
def mergeAllFrames(dataFrames):
    mergedData = None
    return mergedData

# Eric
def mergeFrames(frame1, frame2):
    frame1 = None
    return(mergedFrames)
