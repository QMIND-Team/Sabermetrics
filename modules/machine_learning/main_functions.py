

import modules.machine_learning.feature_selection as fs
import modules.machine_learning.model as model

def printResults(MDAVG, avgRMS,year):
    print("Results for ",year)
    print("The average error is: ",MDAVG)
    print("The RMS is: ",avgRMS)



def featureSelection(df,trainRange,seasonsTested,testedFeatures,toTestFeatures,requiredColumns,target,method):
    testedFeatures, toTestFeatures = fs.getFeatures(df, trainRange, seasonsTested, testedFeatures, toTestFeatures,requiredColumns, 0, target, method)
    print("###########################################################")
    testedFeatures, removed = fs.removeFeatures(df, 5, 5, testedFeatures, requiredColumns, target, method)
    toTestFeatures.extend(removed)
    print("Final Features: ",testedFeatures)

def testSeason(df,target,testedFeatures,requiredColumns,seasonToTest,trainRangeTest,method,showPreds,showRMS,demonstrateModel):
    dfTestColumns = list()

    dfTestColumns.extend(testedFeatures)
    dfTestColumns.extend(requiredColumns)
    dfTest = df[dfTestColumns]

    start = seasonToTest - trainRangeTest
    MDAVG, avgRMS = model.model(target, dfTest, start, seasonToTest, method, showPreds,demonstrateModel)

    if showRMS == 1:
        printResults(MDAVG,avgRMS,seasonToTest)

def testSeasons(df,target,testedFeatures,requiredColumns,trainRangeTest,method,showPreds,showRMS,numberOfSeasons,lastSeason,demonstrateModel):

    for i in range(numberOfSeasons):
        testSeason(df,target,testedFeatures,requiredColumns,lastSeason-i,trainRangeTest,method,showPreds,showRMS,demonstrateModel)



