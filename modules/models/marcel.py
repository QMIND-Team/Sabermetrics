import pandas as pd
import numpy as np
import modules.data_processing.data_cleaning as dc

def runMarcel(marcelDF, stats, roster, league, dateRange):

    dates = dc.convertDateStringToInt(dateRange)
    firstDate = dates[1]
    secondDate = dates[1] - 1
    thirdDate = dates[0]

    if league == 'al':
        lev = 'MLB-AL'
    elif league == 'nl':
        lev = 'MLB-NL'

    leagueDF = marcelDF[marcelDF['Lev'] == lev]
    lgSeason1DF = leagueDF[leagueDF['Year'] == firstDate]
    lgSeason2DF = leagueDF[leagueDF['Year'] == secondDate]
    lgSeason3DF = leagueDF[leagueDF['Year'] == thirdDate]

    firstAvg = leagueAverage(lgSeason1DF, 0)
    secondAvg = leagueAverage(lgSeason2DF, 0)
    thirdAvg = leagueAverage(lgSeason3DF, 0)

    season1DF = marcelDF[marcelDF['Year'] == firstDate]
    season2DF = marcelDF[marcelDF['Year'] == secondDate]
    season3DF = marcelDF[marcelDF['Year'] == thirdDate]

    # set search parameters
    season1DF.set_index("Name", inplace=True)
    season2DF.set_index("Name", inplace=True)
    season3DF.set_index("Name", inplace=True)

    rosterNames = list(roster["Name"])
    statsPlus = ["IP"]
    statsPlus.extend(stats)
    stats1DF = season1DF[statsPlus].replace([np.inf, -np.inf], np.nan).dropna()
    stats2DF = season2DF[statsPlus].replace([np.inf, -np.inf], np.nan).dropna()
    stats3DF = season3DF[statsPlus].replace([np.inf, -np.inf], np.nan).dropna()

    print(stats1DF["SO9"].max())
    print(stats1DF["ERA"].max())
    print(stats1DF["WHIP"].max())

    predictDF = pd.DataFrame(index=rosterNames, columns=stats)

    for player in rosterNames:
        for stat in stats:
            predictDF.at[player, stat] = marcelModel(stat, player, stats1DF, stats2DF,
                                                     stats3DF, firstAvg, secondAvg,thirdAvg)

    print(predictDF)
    return predictDF
def marcelModel(stat, playerId, firstDf, secondDf, thirdDf, firstAvg, secondAvg, thirdAvg):

    # gather data for requested player in each season
    try:
        firstData = firstDf.loc[playerId]
        firstStat = firstData.loc[stat]
        firstIP = firstData.loc['IP']
    except KeyError:
        firstStat = 0
        firstIP = 0
    try:
        secondData = secondDf.loc[playerId]
        secondStat = secondData.loc[stat]
        secondIP = secondData.loc['IP']
    except KeyError:
        secondStat = 0
        secondIP = 0
    try:
        thirdData = thirdDf.loc[playerId]
        thirdStat = thirdData.loc[stat]
        thirdIP = thirdData.loc['IP']
    except KeyError:
        thirdStat = 0
        thirdIP = 0

    # calculate stat value used in calculations
    projStatValue = (firstStat*3)+(secondStat*2)+(thirdStat*1)

    # starting pitcher innings pitched value used in calculations
    projIP = (firstIP * 0.5) + (secondIP * 0.1) + 60

    # finding expected stat for each year incorporating total stat to total IP ratio
    expFirst = firstDf[stat].sum() / firstDf['IP'].sum() * firstIP * 3
    expSecond = secondDf[stat].sum() / secondDf['IP'].sum() * secondIP * 2
    expThird = thirdDf[stat].sum() / thirdDf['IP'].sum() * thirdIP * 1

    # sum of the three seasons expected stat
    expStatTotal = expFirst + expSecond + expThird
    expIPTotal = (firstIP * 3) + (secondIP * 2) + (thirdIP * 1)

    # calculate stat per IP ratio
    regressedStatTotal = expStatTotal / expIPTotal * 900

    statPerIP = (regressedStatTotal + projStatValue) / (900 + expIPTotal) / 2

    # getting the predicted stat output using the stat per IP ratio and the predicted IP calculated
    prediction = statPerIP * projIP
    return prediction

# If perGame equals 1, then the averages will be calculated per game
def leagueAverage(df, perGame):
    dictionary = {}
    if perGame == 1:
        df = dc.perGameConversionAll(df, 1)
    for column in df:
        if type(df[column].values[0]) != str:
            dictionary[column] = df[column].mean()
    return dictionary
