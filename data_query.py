import pybaseball as bball
import pandas as pd

def query(pitcherId, stats, range, league, aggregate):
    statsType = checkStatsFiles(stats)

def checkStatsFiles(stats):
    statsToUse = None
    return(statsToUse)

def statcastData(pitcherId, stats, range):
    statcastData = bball.statcast_pitcher(range[0], range[1], pitcherId)
    statcastDF = pd.DataFrame(statcastDF)
    statsOnly = statcastDF[stats]
    return(statsOnly)

def teamPitchingData(teamName, range, stats, league, aggregate):
    data = None
    return(data)

def bWarData(pitcherId, range, stats):
    data = None
    return(data)

def pitchingFangraphsData(pitcherId, range, stats):
    data = None
    return(data)

def pitchingBrefData(pitcher):
    data = None
    return(data)

def mergeData(dataFrames):
    mergedData = None
    return mergedData