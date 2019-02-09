
import xgboost as xgb
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression

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










