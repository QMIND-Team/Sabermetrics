
import modules.machine_learning.feature_selection as fs
import modules.machine_learning.model as model
import pandas as pd
import modules.data_processing.data_cleaning as dc
import modules.machine_learning.predicted_features_model as pfm


def printResults(MDAVG, avgRMS,year):
    print("Results for ",year)
    print("The average error is: ",MDAVG)
    print("The RMSE is: ",avgRMS)



def featureSelection(df,trainRange,seasonsTested,testedFeatures,toTestFeatures,requiredColumns,target,method):

    testedFeatures, removed = fs.removeFeatures(df, 5, 5, testedFeatures, requiredColumns, target, method)
    toTestFeatures.extend(removed)
    print("###########################################################")

    testedFeatures, toTestFeatures = fs.getFeatures(df, trainRange, seasonsTested, testedFeatures, toTestFeatures,requiredColumns, 0, target, method)

    print("Final Features: ",testedFeatures)

def testSeason(df,target,testedFeatures,requiredColumns,seasonToTest,trainRangeTest,method,showPreds,showRMS,demonstrateModel,givePredictions,showPredictions):
    dfTestColumns = list()

    dfTestColumns.extend(testedFeatures)
    dfTestColumns.extend(requiredColumns)
    dfTest = df[dfTestColumns]

    start = seasonToTest - trainRangeTest
    MDAVG, avgRMS, predictions = model.model(target, dfTest, start, seasonToTest, method, showPreds,demonstrateModel,givePredictions)

    if showRMS == 1:
        printResults(MDAVG,avgRMS,seasonToTest)
    if showPredictions ==1:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(predictions)

def testSeasons(df, target, testedFeatures, requiredColumns, seasonToTest, trainRangeTest, method, showPreds, showRMS, demonstrateModel, givePredictions, showPredictions,numberOfSeasons):

    for i in range(numberOfSeasons):
        testSeason(df, target, testedFeatures, requiredColumns, seasonToTest-i, trainRangeTest, method, showPreds,showRMS, demonstrateModel, givePredictions, showPredictions)