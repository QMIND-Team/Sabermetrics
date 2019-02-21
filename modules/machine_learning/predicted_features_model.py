import modules.machine_learning.help_model as hm
import modules.machine_learning.machine_learning  as ml
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd
from sklearn import preprocessing


def predictedFeaturesModel(targetFeature, df, method,end,trainRange,showPreds):

    df = df.fillna(df.median())


    trainX = df[df.Season < end] # Remove the last season from the train data

   # print("max: ",trainX["Season"].max())
    #print("min: ",trainX["Season"].min())
    max = trainX["Season"].max()
    min = max-trainRange
    trainX = trainX[trainX.Season>min]

    trainY = trainX[targetFeature] # Team and Season are required for later sorting
    trainY = pd.DataFrame(trainY)

   # print("max: ",trainX["Season"].max())
    #print("min: ",trainX["Season"].min())

    trainX = trainX.drop([targetFeature], axis=1)

    trainX = hm.get_numerical_data(trainX)
    trainX = preprocessing.scale(trainX)
    trainX = pd.DataFrame(trainX)

    #The same  process is used for the test data

    testX = df[df.Season == end]
    showPreds = testX[["Team", "Season",targetFeature]] # used to show the results of the model
    showPreds['Season'] = end

    testY = testX[targetFeature]
    testY = pd.DataFrame(testY)
    testX = testX.drop([targetFeature], axis=1)
    testX = hm.get_numerical_data(testX)
    testX = preprocessing.scale(testX)
    testX = pd.DataFrame(testX)

    trainX = trainX.fillna(trainX.median())
    trainY = trainY.fillna(trainY.median())
    testY = testY.fillna(testY.median())

    if method == "XGB":
        preds = ml.XGB(trainX,trainY,testX)
    if method == "LR":
       #preds = ml.linearRegression(trainX,trainY,testX)
        preds = ml.LRFS(trainX,trainY,testX)
    if method == "SVM":
        preds = ml.SVM(trainX,trainY,testX)


    showPreds["prediction"] = preds
    showPreds["difference"] = showPreds[targetFeature] - showPreds["prediction"]
    showPreds["difference"] = showPreds["difference"].abs()
    showPreds = showPreds.sort_values(by="Team", ascending=True)

   # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
      #  print(showPreds)

    meanDifference = showPreds.loc[:, "difference"].mean()
    RMSE = sqrt(mean_squared_error(testY, preds))
    print("++++++++++++++++++")

    return meanDifference, RMSE