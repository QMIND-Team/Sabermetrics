import pitcher_evaluation

# read each line of the parameter file, put each line into an array, store all arrays in parameters
def readParameterFile(filename, parameters):
    parameters = None

# get the team name from the parameters list
def getTeamName(teamName, parameters):
    teamName = None

# get the stats array from the parameters list
def getStats(stats, parameters):
    stats = None

# get the range array from the parameters list
def getRange(range, parameters):
    range = None

# get the league from the parameters list
def getLeague(league, parameters):
    league = None

# get the aggregate condition from the parameters list
def getAggregate(aggregate, parameters):
    aggregate = None

# get the player Ids of all pitchers on the given team name
def getTeamPitchingRoster(teamName, pitcherIds):
    teamName = None

# get pitching evaluations of all pitchers on the given team name
def getPitcherEvaluations(parameters, pitcherEvals):
    stats = None
    teamName = None
    range = None
    league = None
    aggregate = None
    pitcherIds = None

    getTeamName(teamName, parameters)
    getStats(stats, parameters)
    getRange(range, parameters)
    getLeague(league, parameters)
    getAggregate(aggregate, parameters)
    getTeamPitchingRoster(teamName, pitcherIds)
    for i in range(pitcherIds.size()):
        pitcherEvals[i] = pitcherEvaluation(pitcherId[i], teamName, stats, range, league, aggregate)

# for each evaluation type, call the relevant evaluation function
def getEvaluations(playerEvals, parameters):
    evalType = None

filename = None
parameters = None
playerEvals = None

readParameterFile(filename, parameters)
getEvaluations(playerEvals, parameters)



