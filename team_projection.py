import pitcher_evaluation
import csv

# read each line of the parameter file, put each line into an array, store all arrays in parameters
# Vedant
def readParameterFile(filename):
    fileHandle = open(filename) # file handle
    fileReader = csv.reader(fileHandle) # reader object
    contentList = list(fileReader) # list of lists containing the rows
    paramDict = {}
    for row in contentList:
        values = []
        for val in row[1:]: # the first column is the header and the rest are values
            values += [val]
        paramDict[row[0]] = values
    return paramDict

# get the team name from the parameters list
# Will
def getTeamName(teamName, parameters):
    teamName = None

# get the stats array from the parameters list
# Will
def getStats(stats, parameters):
    stats = None

# get the range array from the parameters list
# Will
def getRange(range, parameters):
    dateRange = None

# get the league from the parameters list
# Will
def getLeague(league, parameters):
    league = None

# get the aggregate condition from the parameters list
# Will
def getAggregate(aggregate, parameters):
    aggregate = None

# get the player Ids of all pitchers on the given team name
# Eric
def getTeamPitchingRoster(teamName, pitcherIds):
    teamName = None

# get pitching evaluations of all pitchers on the given team name
# Mike
def getPitcherEvaluations(parameters, pitcherEvals):
    stats = None
    teamName = None
    dateRange = None
    league = None
    aggregate = None
    pitcherIds = None

    getTeamName(teamName, parameters)
    getStats(stats, parameters)
    getRange(dateRange, parameters)
    getLeague(league, parameters)
    getAggregate(aggregate, parameters)
    getTeamPitchingRoster(teamName, pitcherIds)
    for i in range(pitcherIds.size()):
        pitcherEvals[i] = pitcherEvaluation(pitcherId[i], teamName, stats, range, league, aggregate)

# for each evaluation type, call the relevant evaluation function
# Mike
def getEvaluations(playerEvals, parameters):
    evalType = None

filename = None
parameters = None
playerEvals = None

readParameterFile(filename)
getEvaluations(playerEvals, parameters)



