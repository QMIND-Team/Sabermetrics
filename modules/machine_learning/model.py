import modules.machine_learning.help_model as hm
import modules.machine_learning.machine_learning  as ml
import modules.machine_learning.demonstrate_model as dem
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

def model(targetFeature, df, start, end,method,showResult=0,demonstrate=0,givePredictions =0,onlyPredictions =0):

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



    # The learning algorithms that are used in this program use the values of rows in a dataframe to predict a target value in the same row
    # Therefore, the number target feature of the next year must be added to the row that corresponds to the same team from the previous year

    # The nested for loops below adds the target feature from "trainY" in year "z" to the corresponding "trainX" row from year "x-1"
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

    #  The trainY data is now in the  same row as the corresponding trainX data
    #print(trainX)
    trainY = trainX["targetFeature"]
    if demonstrate == 1:
        dem.checkpointFour(trainY)
    trainX = hm.get_numerical_data(trainX)
    if demonstrate == 1:
        dem.checkpointFive(trainX)


    #Important Step

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

    #print(type(trainX))
    #print(type(trainY))
    #print(type(testX))

    if demonstrate ==1:
        dem.checkpointNine()


    if method == "XGB":
        preds = ml.XGB(trainX,trainY,testX)

    if method == "LR":
        preds = ml.LRFS(trainX,trainY,testX)

    if method == "SVM":
        preds = ml.SVM(trainX,trainY,testX)

    if demonstrate==1:
        dem.checkpointTen(method,preds)

    showPreds["prediction"] = preds
    showPreds["difference"] = showPreds["targetFeature"] - showPreds["prediction"]
    showPreds["difference"] = showPreds["difference"].abs()
    showPreds = showPreds.sort_values(by="Team", ascending=True)

    if showResult == 1 and demonstrate != 1:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(showPreds)

    if demonstrate ==1:
        dem.checkpointEleven(showPreds)


    if givePredictions ==1:
        predictions = showPreds[['Team','Season','prediction']]
        predictions.columns = [targetFeature if x == 'prediction' else x for x in predictions.columns]



    testY = testY/1000
    preds = preds/1000
    #print((testY))
    #print((preds))

    meanDifference = showPreds.loc[:, "difference"].mean()
    RMSE = sqrt(mean_squared_error(testY, preds))



    if demonstrate ==1:
        dem.checkpointTwelve(meanDifference,RMSE)
    if demonstrate != 1 :
         print("-----------------") # to show loading
    if onlyPredictions==1:
         return predictions
    else:
        return meanDifference,RMSE,predictions
