
import modules.machine_learning.model as model
import pandas as pd
import modules.data_processing.data_cleaning as dc
import modules.machine_learning.predicted_features_model as pfm
import modules.machine_learning.main_functions as mf

def getPredictions(toPredictFeatures,df,method,end,start,showProcess,rangeToTest):

    #first prediction has to be done outside of the loop so that the merging could happen within the loop

    prediction = pd.DataFrame(columns=['Team','Season'])

    for i in range(0,rangeToTest):
        yearPrediction = pd.DataFrame(columns=['Team', 'Season'])

        for j in toPredictFeatures:
             newPredictions = model.model(j ,df,start-i,end-i,method,givePredictions=1,onlyPredictions =1)
             yearPrediction = dc.mergeFramesHow(yearPrediction, newPredictions, ["Team", "Season"],'outer')
        prediction = prediction.append(yearPrediction)

    columnsTitles = ['Season', 'Team']
    columnsTitles.extend(toPredictFeatures)
    prediction = prediction.reindex(columns=columnsTitles)
    if showProcess == 1:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(prediction)

    return prediction
def advancedModel(toPredictFeatures,df,end,start,showProcess,testRange,targetFeature,method,rangeToTest):
    targetFeatureDf = df[['Season','Team',targetFeature]]
    predictedDf = getPredictions(toPredictFeatures,df,method,end,start,showProcess,rangeToTest)
    predictedDf['Season'] = predictedDf['Season'].astype('float64')
    predictedDf = dc.mergeFramesHow(targetFeatureDf, predictedDf, ["Team", "Season"], 'inner')
    #if showProcess == 1:
       # print("Predicted df")
        #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
          #  print(predictedDf)
    MDAVG, avgRMS = pfm.predictedFeaturesModel(targetFeature,predictedDf,method,end,testRange,showProcess)
    mf.printResults(MDAVG, avgRMS, end)

def runAdvancedModel(toPredictFeature,df,end,start,showProcess,testRange,targetFeature,method,seasonsToTest):
    totalMD =0
    totalRMSE =0
    targetFeatureDf = df[['Season', 'Team', targetFeature]]
    predictedDf = getPredictions(toPredictFeature, df, method, end, start, showProcess, testRange+seasonsToTest)
    predictedDf['Season'] = predictedDf['Season'].astype('float64')
    predictedDf = dc.mergeFramesHow(targetFeatureDf, predictedDf, ["Team", "Season"], 'inner')

    for i in range(seasonsToTest):
        avgMD, avgRMSE = pfm.predictedFeaturesModel(targetFeature, predictedDf, method, end-i, testRange, showProcess)
        #printResults(avgMD, avgRMSE, end-i)
        totalMD = totalMD+ avgMD
        totalRMSE = totalRMSE+avgRMSE

    finalAvgMD = totalMD/seasonsToTest
    finalAvgRMSE = totalRMSE/seasonsToTest

    #print("\nResults for average from ",end-i," to ",end);
    #print("The average error is: ",finalAvgMD)
    #print("The RMSE is: ",finalAvgRMSE)

    return finalAvgMD,finalAvgRMSE

