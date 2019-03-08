import pandas as pd
import csv


# function to create a data frame of MLB 2019 season schedule from a csv
def getSchedule():
    pd.set_option('display.max_columns', 30)  # display all columns in the data frame
    pd.set_option('display.max_rows', 194)  # display all rows in the data frame

    # get excel spreadsheet from http://dailybaseballdata.com/base/sched4.html
    # change directory based on the place the spreadsheet is save to
    schedule = pd.DataFrame.from_csv('/Users/willm/PycharmProjects/Sabermetrics-master/Simulator/MLB_schedule_2019.csv',
                                     header=1, index_col=[0, 1])
    return schedule


# function to get the season schedule for a specific team
def getTeamSchedule(teamName):
    team = toString(teamName)
    schedule = getSchedule()
    drop_cols = list(schedule.columns)
    drop_cols.remove(team)
    teamSchedule = schedule.drop(columns=drop_cols)
    teamSchedule.dropna(inplace=True)
    schedule = toList(teamSchedule)
    return schedule


# function to convert from team name to abbreviated city
def toString(name):
    global team
    if name == 'Angels':
        team = 'Ana'
    elif name == 'Orioles':
        team = 'Bal'
    elif name == 'RedSox':
        team = 'Bos'
    elif name == 'WhiteSox':
        team = 'ChW'
    elif name == 'Indians':
        team = 'Cle'
    elif name == 'Tigers':
        team = 'Det'
    elif name == 'Astros':
        team = 'Hou'
    elif name == 'Royals':
        team = 'Kan'
    elif name == 'Twins':
        team = 'Min'
    elif name == 'Yankees':
        team = 'NYY'
    elif name == 'Athletics':
        team = 'Oak'
    elif name == 'Mariners':
        team = 'Sea'
    elif name == 'Rays':
        team = 'Tam'
    elif name == 'Rangers':
        team = 'Tex'
    elif name == 'BlueJays':
        team = 'Tor'
    elif name == 'Diamondbacks':
        team = 'Ari'
    elif name == 'Braves':
        team = 'Atl'
    elif name == 'Cubs':
        team = 'ChC'
    elif name == 'Reds':
        team = 'Cin'
    elif name == 'Rockies':
        team = 'Col'
    elif name == 'Marlins':
        team = 'Fla'
    elif name == 'Dodgers':
        team = 'Los'
    return team

