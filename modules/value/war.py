
import modules.models.marcel as marcel

def calculateWAR(dfList, playerId):
    df1 = dfList[0]
    df2 = dfList[1]
    df3 = dfList[3]
    WAR1 = calculateWAR1(df1, df2, df3, playerId)
    WAR2 = calculateWAR2(df1, df2, df3, playerId)
    WAR3 = calculateWAR3(df1, df2, df3, playerId)
    return [WAR1, WAR2, WAR3]

def calculateWAR1(df1, df2, df3, playerId):
    # get stats for 3 years needed for war from pe and pass as arg

    # calculate WAR from the stats in each dataframe

    # go through each dataframe
    # create new column for WAR computed from the stats

    dataframeList = [df1, df2, df3]

    for df in dataframeList:

        leagueFIP = marcel.leagueAverage(df, perGame=1)['FIP']

        # calculate replacement level
        df['RL'] =  (0.03 * (1 - (df['GS']/df['G']))) + (0.12 * (df['GS']/df['G']))
        # and leverage index
        df['LI'] = (1 + df['gmLI'])/2

        df['WAR'] = (((((leagueFIP - df['FIP'])/(df['HR'] + df['K'] + df['BB'])) + df['RL']) * df['IP/9']) * df['LI']) + (-0.00095 * df['IP'])

    # pass the three dataframes through marcel and get projections for war
    firstAvg = marcel.leagueAverage(df1, perGame=1)['WAR']
    secondAvg = marcel.leagueAverage(df2, perGame=1)['WAR']
    thirdAvg = marcel.leagueAverage(df3, perGame=1)['WAR']
    mostRecentSeason = df1['Year']
    predictedWAR = marcel.marcelModel('WAR', playerId, mostRecentSeason, firstAvg, secondAvg, thirdAvg)

    return predictedWAR


def calculateWAR2(df1, df2, df3, playerId):
    # get stats for 3 years needed for war from pe and pass as arg

    # pass all three dataframes through marcel and get projections for each stat
    dataframeList = [df1, df2, df3]
    stats = ['FIP', 'BB', ' K', 'HR', 'IP/9', 'G', 'GS', 'gmLI']
    leagueAverageDict1 = marcel.leagueAverage(df1, perGame=1)
    leagueAverageDict2 = marcel.leagueAverage(df2, perGame=1)
    leagueAverageDict3 = marcel.leagueAverage(df3, perGame=1)

    pred = {}

    for stat in stats:
        firstAvg = leagueAverageDict1[stat]
        secondAvg = leagueAverageDict2[stat]
        thirdAvg = leagueAverageDict3[stat]
        mostRecentSeason = df1['Year']
        # playerId =
        pred[stat] = marcel.marcelModel(stat, playerId, mostRecentSeason, firstAvg, secondAvg, thirdAvg)

    # compute war with the projected stats
    # calculate replacement level
    pred['RL'] = (0.03 * (1 - (pred['GS'] / pred['G']))) + (0.12 * (pred['GS'] / pred['G']))
    # and leverage index
    pred['LI'] = (1 + pred['gmLI']) / 2

    predictedWAR = (((((leagueAverageDict1['FIP'] - pred['FIP']) / (pred['HR'] + pred['K'] + pred['BB'])) + pred['RL']) * pred['IP/9']) * pred['LI']) + (
                -0.00095 * pred['IP'])

    return predictedWAR

def calculateWAR3(df1, df2, df3, playerId):
    # get WAR for 3 years and pass as arg

    # pass all 3 dataframes through marcel and get projections for WAR
    leagueAverageDict1 = marcel.leagueAverage(df1, perGame=1)
    leagueAverageDict2 = marcel.leagueAverage(df2, perGame=1)
    leagueAverageDict3 = marcel.leagueAverage(df3, perGame=1)

    firstAvg = leagueAverageDict1['WAR']
    secondAvg = leagueAverageDict2['WAR']
    thirdAvg = leagueAverageDict3['WAR']

    predictedWAR = marcel.marcelModel('WAR', playerId, df1['Year'], firstAvg, secondAvg, thirdAvg)

    return predictedWAR
