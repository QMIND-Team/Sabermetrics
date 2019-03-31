import modules.machine_learning.ml_methods.help_model as hm
import modules.machine_learning.ml_methods.machine_learning  as ml
import modules.machine_learning.main_model.demonstrate_model as dem
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd
from sklearn import preprocessing



def runModel(testDf ,trainRange,seasonsTested ,target,method,showPreds,showFULLRMSE):
    count =0
    totalMD = 0
    totalRMS = 0
    for k in range(seasonsTested):
        start = 2018 - trainRange - k
        end = 2018 - k
        count = count + 1

        MD, RMS = model(target, testDf, start, end,method,showPreds)
        totalMD = totalMD + MD
        totalRMS = totalRMS + RMS
        if showFULLRMSE == 1:
            print(end,"RMS =",RMS)

    MDAVG = totalMD / count
    avgRMS = totalRMS / count

    return MDAVG, avgRMS

def model(targetFeature, df, start, end,method,noPreds=0,demonstrate=0,givePredictions =0,onlyPredictions =0):


    df = df.fillna(df.median())
    df = df[df.Season >= start]
    df = df[df.Season <= end]

    df[targetFeature] = df[targetFeature]*1000
    df[targetFeature] = df[targetFeature].fillna(0.0).astype(int)


    train = df[df.Season != end] # Remove the last season from the train data
    trainX = train[train.Season != (end - 1)] # The last year of the train data can not be used for predictions
    trainY = train[[targetFeature, "Team", "Season"]] # Team and Season are required for later sorting


    if demonstrate == 1:
        dem.checkpointOne(trainX,trainY,end)

    if demonstrate == 1:
        dem.checkpointTwo(trainX,trainY)

    for i in trainX.index:
        seasonX = trainX.loc[i, 'Season']
        teamX = trainX.loc[i, 'Team']
        for j in trainY.index:
            seasonY = trainY.loc[j, 'Season']
            teamY = trainY.loc[j, 'Team']
            if ((seasonX == seasonY - 1) and (teamX == teamY)):
                trainX.loc[i, "targetFeature"] = trainY.loc[j, targetFeature]

    if demonstrate == 1:
        dem.checkpointThree(trainX)

    trainY = trainX["targetFeature"]
    if demonstrate == 1:
        dem.checkpointFour(trainY)
    trainX = hm.get_numerical_data(trainX)
    if demonstrate == 1:
        dem.checkpointFive(trainX)

    trainX = trainX.drop(["targetFeature"], axis=1) #To prevent overfitting, the target feature is dropped from the trainX data
    if demonstrate == 1:
        dem.checkpointSix(trainX)

    trainX = preprocessing.scale(trainX)
    if demonstrate == 1:
        dem.checkpointSeven(trainX)


    #The same  process is used for the test data

    testX = df[df.Season == (end - 1)]
    testY = df[(df.Season == end)]
    if demonstrate ==1:
        dem.checkpointEight(testX,testY,end)

    for i in testX.index:
        seasonX = testX.loc[i, 'Season']
        teamX = testX.loc[i, 'Team']
        for j in testY.index:
            seasonY = testY.loc[j, 'Season']
            teamY = testY.loc[j, 'Team']
            if ((seasonX == seasonY - 1) and (teamX == teamY)):
                testX.loc[i, "targetFeature"] = testY.loc[j, targetFeature]

    showPreds = testX[["Team", "Season","targetFeature"]] # used to show the results of the model
    showPreds['Season'] = end

    testY = testX["targetFeature"]

    testX = testX.drop(["targetFeature"], axis=1)
    testX = hm.get_numerical_data(testX)
    testX = preprocessing.scale(testX)


    if demonstrate ==1:
        dem.checkpointNine()


    if method == "XGB":
        preds = ml.XGB(trainX,trainY,testX)

    if method == "LRFS":
        preds = ml.LRFS(trainX,trainY,testX)

    if method == "SVM":
        preds = ml.SVM(trainX,trainY,testX)

    if method == "LR":
        preds = ml.LR(trainX,trainY,testX)

    if demonstrate==1:
        dem.checkpointTen(method,preds)

    showPreds["prediction"] = preds/1000
    showPreds["targetFeature"] = showPreds["targetFeature"]/1000
    showPreds["difference"] = showPreds["targetFeature"] - showPreds["prediction"]
    showPreds["difference"] = showPreds["difference"].abs()
    showPreds = showPreds.sort_values(by="Team", ascending=True)


    if demonstrate ==1:
        dem.checkpointEleven(showPreds)

    if givePredictions ==1:
        predictions = showPreds[['Team','Season','prediction']]
        predictions.columns = [targetFeature if x == 'prediction' else x for x in predictions.columns]

    testY = testY/1000
    preds = preds/1000


    meanDifference = showPreds.loc[:, "difference"].mean()
    testY = testY.fillna(testY.median())

    RMSE = sqrt(mean_squared_error(testY, preds))

    print("--------------")
    if onlyPredictions ==1:
        return predictions

    if noPreds ==1:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(showPreds)
            return meanDifference,RMSE,preds

    return meanDifference,RMSE
