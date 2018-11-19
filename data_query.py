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
    data = None
    return(data)

def bWarData(pitcherId, dateRange, stats):
    data = None
    return(data)

def pitchingFangraphsData(pitcherId, dateRange, stats):
    data = None
    return(data)

def pitchingBrefData(pitcher):
    data = None
    return(data)

# Eric
def mergeAllFrames(dataFrames):
    mergedData = None
    return mergedData

# Eric
def mergeFrames(frame1, frame2):
    frame1 = None
    return(mergedFrames)
