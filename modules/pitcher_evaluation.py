import modules.data_processing.data_query as dq
import modules.models.marcel as marcel
import pandas as pd
import numpy as np

# get pitching evaluations of all pitchers on the given team name
def getPitcherEvaluations(parameters):
    predictStats = runModel(parameters)
    print(predictStats)
    return 0

def runModel(parameters):
    model = getModel(parameters)
    if model == 'marcel':
        roster = getTeamPitchingRoster(parameters)
        stats = getStats(parameters)
        league = getLeague(parameters)
        dateRange = getDateRange(parameters)
        marcelDF = prepareMarcelData(parameters)

        predictDF = marcel.runMarcel(marcelDF, stats, roster, league, dateRange)
        return predictDF

def prepareMarcelData(parameters):
    source =  getSource(parameters)
    dateRange = getDateRange(parameters)
    stats = getStats(parameters)

    marcelStats = ["Name", "Age", "Year", "G", "GS", "IP"]
    marcelStats.extend(stats)

    marcelDF = dq.query(source, marcelStats, dateRange)
    return marcelDF

# get the player Ids of all pitchers on the given team name
def getTeamPitchingRoster(parameters):
    dateRange = getDateRange(parameters)
    teamName = getTeamName(parameters)
    stats = ["Tm", "Name", "IP"]

    data = dq.pitchingBaseballSavantData(dateRange,stats)
    df = pd.DataFrame(data)
    df = df.loc[df['Tm'] == teamName]
    df = df.loc[df['IP'] >= 10]
    df = df[['Name']]
    return df

# get the team name from the parameters list
def getTeamName(parameters):
    teamName = parameters['team'][0]
    return teamName

def getSource(parameters):
    source = parameters['source'][0]
    return source

def getModel(parameters):
    model = parameters['model'][0]
    return model

# get the stats array from the parameters list
def getStats(parameters):
    stats = parameters['stats']
    return stats

# get the range array from the parameters list
def getDateRange(parameters):
    dateRange = parameters['dateRange']
    return dateRange

# get the league from the parameters list
def getLeague(parameters):
    league = parameters['league'][0]
    return league

# get the aggregate condition from the parameters list
def getAggregate(parameters):
    aggregate = parameters['aggregate'][0]
    return aggregate
