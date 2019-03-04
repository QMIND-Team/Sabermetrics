
import xgboost as xgb
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

from sklearn.feature_selection import SelectPercentile
from sklearn.linear_model import LogisticRegression
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
import modules.machine_learning.help_model as hm

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


def linearRegression(trainX,trainY,testX):

    regressor = LinearRegression()
    regressor.fit(trainX, trainY)
    preds = regressor.predict(testX)

    return preds

def XGB(trainX,trainY,testX):
    xg_cl = xgb.XGBClassifier()
    xg_cl.fit(trainX, trainY)
    preds = xg_cl.predict(testX)
    return preds

def SVM(trainX,trainY,testX):
    clf = svm.SVC(kernel="linear", C=1.0)
    clf.fit(trainX, trainY)
    preds = clf.predict(testX)
    return  preds



def LRFS(trainX,trainY,testX,testY):

    lr = LinearRegression()

    numberOfFeaturesArray = trainX.shape

    numberOfFeatures  = numberOfFeaturesArray[1]

    bestRMSE = 100000000

    for i in range(1,numberOfFeatures):

        sel = RFE(estimator= lr,n_features_to_select=i)
        sol = sel.fit(trainX,trainY)


        X_new_app = trainX[:,sol.support_]
        #print(X_new_app.shape)
        moc = lr.fit(X_new_app,trainY)

        X_new_test = testX[:,sol.support_]

        preds = mod.predict(X_new_test)

        RMSE = test(preds,testY)

        if (RMSE < bestRMSE):
            bestRMSE = RMSE
            bestPreds = preds
            #print(bestRMSE)
    #print("final RMSE: ")
    #print(bestRMSE)

    return bestPreds



def test(preds,testY):

    RMSE = sqrt(mean_squared_error(testY, preds))

    return RMSE
