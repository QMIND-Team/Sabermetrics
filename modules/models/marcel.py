import pandas as pd
import numpy as np
from pybaseball import pitching_stats_bref
import modules.data_processing.data_cleaning as dc


def marcel_model(Stat, PlayerID, mostRecentSeason, first_avg, second_avg, third_avg):
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
    first_data = first_df.loc[PlayerID]
    second_data = second_df.loc[PlayerID]
    third_data = third_df.loc[PlayerID]

    # get IP stat for requested player in each season
    first_IP = first_data.loc['IP']
    second_IP = second_data.loc['IP']
    third_IP = third_data.loc['IP']

    # get requested stat of player in each season
    first_stat = first_data.loc[Stat]
    second_stat = second_data.loc[Stat]
    third_stat = third_data.loc[Stat]

    # calculate stat value used in calculations
    #stat = (first_stat*5)+(second_stat*4)+(third_stat*3)

    # starting pitcher innings pitched value used in calculations
    IP = (first_IP*0.5)+(second_IP*0.1)+60

    # finding expected stat for each year incorporating total stat to total IP ratio
    exp_first = first_avg*first_stat*5
    exp_second = second_avg*second_stat*4
    exp_third = third_avg*third_stat*3

    # sum of the three seasons expected stat
    exp_stat = exp_first + exp_second + exp_third

    # calculate stat per IP ratio
    stat_per_IP = exp_stat/stat

    # getting the predicted stat output using the stat per IP ratio and the predicted IP calculated
    prediction = stat_per_IP * IP

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
    df1 = pitching_stats_bref(season1)
    df2 = pitching_stats_bref(season2)
    df3 = pitching_stats_bref(season3)

    # set index of the DataFrames to Name
    df1 = df1.set_index('Name')
    df2 = df2.set_index('Name')
    df3 = df3.set_index('Name')

    # stats from last 3 seasons
    # update to convert name to player_id?
    player_stats1 = df1.loc[player_name]
    player_stats2 = df2.loc[player_name]
    player_stats3 = df3.loc[player_name]

    # required stats from last 3 seasons
    stats1 = player_stats1.loc[stats]
    stats2 = player_stats2.loc[stats]
    stats3 = player_stats3.loc[stats]

    # weighted stats
    # highest weight for latest season
    weight = 5
    for i in [stats1, stats2, stats3]:
        i *= weight
        weight -= 1

