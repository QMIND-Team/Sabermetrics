

'''

NOT DONE YET, DO NOT USE


'''

import modules.machine_learning.help_model as hm
import modules.machine_learning.machine_learning  as ml
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd
from sklearn import preprocessing

def predictedFeaturesModel(targetFeature, df, method,trainRange,showResult):

    df = df.fillna(df.median())

    df[targetFeature] = df[targetFeature]*1000
    df[targetFeature] = df[targetFeature].fillna(0.0).astype(int)

    trainX = df[df.Season < 2019] # Remove the last season from the train data


    max = trainX["Season"].max()
    min = max-trainRange
    trainX = trainX[trainX.Season>min]

    trainY = trainX[targetFeature] # Team and Season are required for later sorting
    trainY = pd.DataFrame(trainY)

    trainX = trainX.drop([targetFeature], axis=1)

    trainX = hm.get_numerical_data(trainX)
    trainX = preprocessing.scale(trainX)
    trainX = pd.DataFrame(trainX)

    #The same  process is used for the test data

    testX = df[df.Season == 2019]
    showPreds = testX[["Team", "Season",targetFeature]] # used to show the results of the model
    showPreds['Season'] = 2019

    #testY = testX[targetFeature]
    #testY = pd.DataFrame(testY)
    testX = testX.drop([targetFeature], axis=1)
    testX = hm.get_numerical_data(testX)
    testX = preprocessing.scale(testX)
    testX = pd.DataFrame(testX)

    trainX = trainX.fillna(trainX.median())
    trainY = trainY.fillna(trainY.median())
    #testY = testY.fillna(testY.median())

    trainX = trainX.values
    trainY = trainY.values
    testX = testX.values

    if method == "XGB":
        preds = ml.XGB(trainX,trainY,testX)
    if method == "LR":
        #preds = ml.linearRegression(trainX,trainY,testX)
        preds = ml.LRFS(trainX,trainY,testX,testY)
    if method == "SVM":
        preds = ml.SVM(trainX,trainY,testX)

    testY[targetFeature] = testY[targetFeature] / 1000
    preds = preds / 1000


    if showResult == 1:
        showPreds["prediction"] = preds
        showPreds["difference"] = showPreds[targetFeature] - showPreds["prediction"]
        showPreds["difference"] = showPreds["difference"].abs()
        showPreds = showPreds.sort_values(by="Team", ascending=True)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(showPreds)


def getFeatures(targetFeature, df, start, method, showResult):
    df = df.fillna(df.median())
    df = df[df.Season >= start]

    df[targetFeature] = df[targetFeature] * 1000
    df[targetFeature] = df[targetFeature].fillna(0.0).astype(int)

    train = df[df.Season != 2018]  # Remove the last season from the train data
    trainX = train[train.Season != (2018 - 1)]  # The last year of the train data can not be used for predictions
    trainY = train[[targetFeature, "Team", "Season"]]  # Team and Season are required for later sorting


    for i in trainX.index:
        seasonX = trainX.loc[i, 'Season']
        teamX = trainX.loc[i, 'Team']
        for j in trainY.index:
            seasonY = trainY.loc[j, 'Season']
            teamY = trainY.loc[j, 'Team']
            if ((seasonX == seasonY - 1) and (teamX == teamY)):
                trainX.loc[i, "targetFeature"] = trainY.loc[j, targetFeature]

    trainY = trainX["targetFeature"]
    trainX = hm.get_numerical_data(trainX)



    trainX = trainX.drop(["targetFeature"], axis=1)  # To prevent overfitting, the target feature is dropped from the trainX data


    trainX = preprocessing.scale(trainX)


    testX = df[df.Season == (2018)]


    showPreds = testX[["Team", "Season", "targetFeature"]]  # used to show the results of the model
    showPreds['Season'] = end


    testX = testX.drop(["targetFeature"], axis=1)
    testX = hm.get_numerical_data(testX)
    testX = preprocessing.scale(testX)



    if method == "XGB":
        preds = ml.XGB(trainX, trainY, testX)

    if method == "LR":
        preds = ml.LRFS(trainX, trainY, testX, testY)

    if method == "SVM":
        preds = ml.SVM(trainX, trainY, testX)


    showPreds["prediction"] = preds
    showPreds = showPreds.sort_values(by="Team", ascending=True)

    if showResult == 1:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(showPreds)



    testY = testY / 1000
    preds = preds / 1000

    return preds