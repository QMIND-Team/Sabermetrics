import modules.pitcher_evaluation as pitch
import csv

# read each line of the parameter file, put each line into an array, store all arrays in parameters
def readParameterFile(filename):
    fileHandle = open(filename) # file handle
    fileReader = csv.reader(fileHandle, delimiter=',', skipinitialspace=True) # reader object
    contentList = list(fileReader) # list of lists containing the rows
    paramDict = {}
    for row in contentList:
        values = []
        for val in row[1:]: # the first column is the header and the rest are values
            values += [val]
        paramDict[row[0]] = values
    return paramDict

# for each evaluation type, call the relevant evaluation function
def getEvaluations(parameters):
    evalDict = {"pitching": [],
                "batting": [],
                "fielding": []}
    if "pitching" in parameters:
        evalDict["pitching"] = pitch.getPitcherEvaluations(parameters)
    return evalDict

filename = "modules/csv/parameters_template.csv"

parameters = readParameterFile(filename)
evaluations = getEvaluations(parameters)



