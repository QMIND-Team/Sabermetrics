import Simulator
import warnings
import pandas as pd
import numpy as np

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['getSchedule', 'getTeamSchedule', 'toString', 'toName', 'toList', 'checkFirstBit', 'homeOrAway']

# ignore warnings in code
warnings.simplefilter("ignore")


def gamesByDate(date):
    pd.set_option("display.max_columns", 31)
    schedule = getSchedule()
    givenDate = splitDate(date)
    schedule.reset_index(level='2019', inplace=True)
    gamesByDay = schedule[schedule['2019'] == givenDate]
    return gamesByDay


# function to create a data frame of MLB 2019 season schedule from a csv
def getSchedule():
    pd.set_option('display.max_columns', 31)  # display all columns in the data frame
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


# splits an input date in dd/mm form into the form used in getSchedule()
def splitDate(date):
    schedule = getSchedule()
    gameDateList = schedule.index.get_level_values('2019')
    dateList = date.split("/")
    dateArray = np.array(dateList)
    day = int(dateArray[0])
    month = int(dateArray[1])
    month = toMonth(month)
    givenDate = toDateStr(day, month)
    return givenDate


# converting from integer version of month to short hand of month name
def toMonth(month):
    switcher = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return switcher.get(month, "Invalid Month")


# format the output to match index in schedule
def toDateStr(day, month):
    return "{}-{}".format(day, month)


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


# function to convert from abbreviated city to team name
def toName(city):
    global teamName
    if city == 'Ana':
        teamName = 'Angels'
    elif city == 'Bal':
        teamName = 'Orioles'
    elif city == 'Bos':
        teamName = 'RedSox'
    elif city == 'ChW':
        teamName = 'WhiteSox'
    elif city == 'Cle':
        teamName = 'Indians'
    elif city == 'Det':
        teamName = 'Tigers'
    elif city == 'Hou':
        teamName = 'Astros'
    elif city == 'Kan':
        teamName = 'Royals'
    elif city == 'Min':
        teamName = 'Twins'
    elif city == 'NYY':
        teamName = 'Yankees'
    elif city == 'Oak':
        teamName = 'Athletics'
    elif city == 'Sea':
        teamName = 'Mariners'
    elif city == 'Tam':
        teamName = 'Rays'
    elif city == 'Tex':
        teamName = 'Rangers'
    elif city == 'Tor':
        teamName = 'BlueJays'
    elif city == 'Ari':
        teamName = 'Diamondbacks'
    elif city == 'Atl':
        teamName = 'Braves'
    elif city == 'ChC':
        teamName = 'Cubs'
    elif city == 'Cin':
        teamName = 'Reds'
    elif city == 'Col':
        teamName = 'Rockies'
    elif city == 'Fla':
        teamName = 'Marlins'
    elif city == 'Los':
        teamName = 'Dodgers'
    return teamName


# function to creates a list of all the games a given team will play in a season
def toList(dataFrame):
    games = pd.DataFrame(dataFrame)
    return games.values.tolist()


# function to slice the contents of the list, removing all []'s and ''s
def checkFirstBit(teamSchedule):
    for i in range(len(teamSchedule)):
        team = str(teamSchedule[i])
        team = team[2:6]
        if team[0] == "@":
            sliced = team[1:4]
            teamSchedule[i] = sliced
        elif team[0] != "@":
            sliced = team[0:3]
            teamSchedule[i] = sliced
    return teamSchedule


# function to check the first bit of each element to determine if it is a home or away game
def homeOrAway(teamSchedule):
    home_lst = []
    for i in range(len(teamSchedule)):
        team = str(teamSchedule[i])
        team = team[2:6]
        if team[0] == "@":
            home = "False"
        else:
            home = "True"
        home_lst.append(home)
    return home_lst


gamesByDate("15/06")
