

import pybaseball as bball
import modules.data_processing.data_cleaning as dc
import modules.data_processing.data_query as dq


def getAll(start,end):
    #df1 = bball.team_pitching(start, end)
    df1 = dq.teamPitching(start, end)
    #df2 = bball.team_batting(start_season=start, end_season=end, league='all', ind=1)
    df2 = dq.teamBatting(start, end)

    dfAll = dc.mergeFramesHow(df1, df2, ["Team", "Season"],'inner')
    #print(dfAll.columns)
    return dfAll

def getSortedFeatures(testedFeatures,requiredColumns,allFeatures):

    toTestFeatures =allFeatures.drop(requiredColumns)
    toTestFeatures =toTestFeatures.drop(testedFeatures)

    toTestFeatures = list(toTestFeatures) #features that need to be tested before being added to tested features

    return toTestFeatures
