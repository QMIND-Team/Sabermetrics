
import xgboost as xgb
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.feature_selection import RFE

def LR(trainX,trainY,testX):
    trainY = trainY.fillna(trainY.median())

    regressor = LinearRegression()
    regressor.fit(trainX, trainY)
    preds = regressor.predict(testX)
    return preds



def LRFS(trainX,trainY,testX):
    trainY = trainY.fillna(trainY.median())

    numberOfFeaturesArray = trainX.shape

    numberOfFeatures  = numberOfFeaturesArray[1]

    #    trainY = trainY.fillna(trainY.median())

    #print(type(trainX))
    #print(type(trainY))
    trainY = trainY.fillna(trainY.median())

    lr = LinearRegression()

    sel = RFE(estimator=lr,n_features_to_select = int(numberOfFeatures*0.8))
    fit = sel.fit(trainX, trainY)

    X_new_app = trainX[:, fit.support_]

    mod = lr.fit(X_new_app, trainY)

    X_new_test = testX[:, fit.support_]

    preds = mod.predict(X_new_test)


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



def test(preds,testY):

    RMSE = sqrt(mean_squared_error(testY, preds))

    return RMSE
