import pandas as pd
import numpy as np

from pybaseball import pitching_stats_bref


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
