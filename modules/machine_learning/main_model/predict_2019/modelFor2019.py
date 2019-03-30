import modules.machine_learning.ml_methods.help_model as hm
import modules.machine_learning.ml_methods.machine_learning  as ml
import pandas as pd
from sklearn import preprocessing




def model2019(targetFeature, df, start,method):
    df = df.fillna(df.median())
    df = df[df.Season >= start]
    df = df[df.Season <= 2018]

    df[targetFeature] = df[targetFeature]*1000
    df[targetFeature] = df[targetFeature].fillna(0.0).astype(int)

    train = df
    trainX = train[train.Season != (2018)] # The last year of the train data can not be used for predictions
    trainY = train[[targetFeature, "Team", "Season"]] # Team and Season are required for later sorting

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


    trainX = trainX.drop(["targetFeature"], axis=1) #To prevent overfitting, the target feature is dropped from the trainX data


    trainX = preprocessing.scale(trainX)


    #The same  process is used for the test data

    testX = df[df.Season == (2018)]

    showPreds = pd.DataFrame(testX["Team"])


    testX = hm.get_numerical_data(testX)
    testX = preprocessing.scale(testX)

    if method == "XGB":
        preds = ml.XGB(trainX,trainY,testX)

    if method == "LR":
        preds = ml.LR(trainX,trainY,testX)

    if method == "SVM":
        preds = ml.SVM(trainX,trainY,testX)
    if method == "LRFS":
        preds = ml.LRFS(trainX,trainY,testX)


    showPreds["Target"]= preds/1000

    showPreds = showPreds.sort_values(by="Target", ascending=False)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(showPreds)


