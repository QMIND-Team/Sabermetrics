import pandas as pd
import numpy as np
import pybaseball as bball
# from pybaseball import pitching_stats_bref
import modules.data_processing.data_cleaning as dc

def marcelModel(stat, playerId, mostRecentSeason, firstAvg, secondAvg, thirdAvg):
    # get stats for 3 previous seasons
    #first_season = pitching_stats_bref(mostRecentSeason)
    #second_season = pitching_stats_bref(mostRecentSeason-1)
    #third_season = pitching_stats_bref(mostRecentSeason-2)

    # create Data Frames for these seasons
    #first_df = pd.DataFrame(first_season)
    #second_df = pd.DataFrame(second_season)
    #third_df = pd.DataFrame(third_season)

    # set search parameters
    #first_df.set_index("Name", inplace=True)
    #second_df.set_index("Name", inplace=True)
    #third_df.set_index("Name", inplace=True)

    # gather data for requested player in each season
    firstData = firstDF.loc[playerId]
    secondData = secondDF.loc[playerId]
    thirdData = thirdDF.loc[playerId]

    # get IP stat for requested player in each season
    firstIP = firstData.loc['IP']
    secondIP = secondData.loc['IP']
    thirdIP = thirdData.loc['IP']

    # get requested stat of player in each season
    firstStat = firstData.loc[stat]
    secondStat = secondData.loc[stat]
    thirdStat = thirdData.loc[stat]

    # calculate stat value used in calculations
    #stat = (firstStat*5)+(secondStat*4)+(thirdStat*3)

    # starting pitcher innings pitched value used in calculations
    IP = (firstIP*0.5)+(secondIP*0.1)+60

    # finding expected stat for each year incorporating total stat to total IP ratio
    expFirst = firstAvg*firstStat*5
    expSecond = secondAvg*secondStat*4
    expThird = thirdAvg*thirdStat*3

    # sum of the three seasons expected stat
    expStat = expFirst + expSecond + expThird

    # calculate stat per IP ratio
    statPerIP = expStat/stat

    # getting the predicted stat output using the stat per IP ratio and the predicted IP calculated
    prediction = statPerIP * IP

    return prediction

#If perGame equals 1, then the averages will be calculated per game
def leagueAverage(df,perGame):
    dictionary = {}
    if(perGame ==1):
        df = dc.perGameConversionAll(df, 1)
    for column in df:
        if(type(df[column].values[0]) != str):
                dictionary[column] = df[column].mean()
    return dictionary

def assign_weights(stats, player_name, season):
    # last 3 seasons
    season1 = season - 1
    season2 = season - 2
    season3 = season - 3

    # DataFrames for last 3
    #  update to take data after cleaning
    df1 = bball.pitching_stats_bref(season1)
    df2 = bball.pitching_stats_bref(season2)
    df3 = bball.pitching_stats_bref(season3)

    # set index of the DataFrames to Name
    df1 = df1.set_index('Name')
    df2 = df2.set_index('Name')
    df3 = df3.set_index('Name')

    # stats from last 3 seasons
    # update to convert name to player_id?
    playerStats1 = df1.loc[player_name]
    playerStats2 = df2.loc[player_name]
    playerStats3 = df3.loc[player_name]

    # required stats from last 3 seasons
    stats1 = playerStats1.loc[stats]
    stats2 = playerStats2.loc[stats]
    stats3 = playerStats3.loc[stats]

    # weighted stats
    # highest weight for latest season
    weight = 5
    for i in [stats1, stats2, stats3]:
        i *= weight
        weight -= 1
