

import pybaseball as bball
import modules.data_processing.data_cleaning as dc


def getAll(start,end):
    df1 = bball.team_pitching(start, end)
    df2 = bball.team_batting(start_season=start, end_season=end, league='all', ind=1)

    dfAll = dc.mergeFrames(df1, df2, ["Team", "Season"])

    return dfAll

def getSortedFeatures(testedFeatures,requiredColumns,allFeatures):

    toTestFeatures =allFeatures.drop(requiredColumns)
    toTestFeatures =toTestFeatures.drop(testedFeatures)

    toTestFeatures = list(toTestFeatures) #features that need to be tested before being added to tested features

    return toTestFeatures
