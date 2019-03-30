
import modules.machine_learning.ml_methods.model as model
import pandas as pd
import modules.data_processing.data_cleaning as dc
import modules.machine_learning.advanced_model.predicted_features_model as pfm
import modules.machine_learning.main_model.main_functions as mf

def getPredictions(toPredictFeatures,df,method,end,start,showProcess,testRange):
    prediction = pd.DataFrame(columns=['Team','Season'])

    for i in range(0,end-start+1):
        yearPrediction = pd.DataFrame(columns=['Team', 'Season'])

        for j in toPredictFeatures:

             newPredictions = model.model(j, df, end - i - testRange, end - i, method, givePredictions=1, onlyPredictions =1)
             yearPrediction = dc.mergeFramesHow(yearPrediction, newPredictions, ["Team", "Season"],'outer')
        prediction = prediction.append(yearPrediction)

    columnsTitles = ['Season', 'Team']
    columnsTitles.extend(toPredictFeatures)
    prediction = prediction.reindex(columns=columnsTitles)

    return prediction
def advancedModel(features,df,end,start,showProcess,testRange,targetFeature,method,rangeToTest):
    targetFeatureDf = df[['Season','Team',targetFeature]]
    predictedDf = getPredictions(features,df,method,end,start+rangeToTest,showProcess,rangeToTest)

    print("here")
    predictedDf['Season'] = predictedDf['Season'].astype('float64')
    predictedDf = dc.mergeFramesHow(targetFeatureDf, predictedDf, ["Team", "Season"], 'inner')

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
        totalMD = totalMD+ avgMD
        totalRMSE = totalRMSE+avgRMSE

        print("The RMSE is",avgRMSE)



    finalAvgMD = totalMD/seasonsToTest
    finalAvgRMSE = totalRMSE/seasonsToTest

    print("\nResults for average from ",end-i," to ",end);
    print("The average error is: ",finalAvgMD)
    print("The RMSE is: ",finalAvgRMSE)

    return finalAvgMD,finalAvgRMSE

