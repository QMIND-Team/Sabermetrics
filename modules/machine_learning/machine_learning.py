
import xgboost as xgb
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
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

    '''
    lr = LinearRegression()
    rfe = RFE(lr, n_features_to_select=1)
    rfe.fit(trainX, trainY)

    print("Features sorted by their rank:")
    print(rfe.ranking_)


    select = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold='median')

    select.fit(trainX, trainY)

    trainXS = select.transform(trainX)
    print('The shape of X_train is: ', trainX.shape)
    print('The shape of X_train_s is ', trainXS.shape)

    testXS = select.transform(testX)
    regressor = LinearRegression()
    regressor.fit(trainXS,trainY)
    preds = regressor.predict(testXS)
    print(select.
    
    '''
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


from sklearn.feature_selection import RFECV


from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso

'''
def LRFS(trainX,trainY,testX):
    estimator = Lasso()
    featureSelection = SelectFromModel(estimator)
    featureSelection.fit(trainX, trainY)
    selectedFeatures = featureSelection.transform(trainX)
    print(selectedFeatures)
    print(trainX.columns[featureSelection.get_support()])
'''

'''
def LRFS(trainX,trainY,testX):
    clf_rf_4 = RandomForestClassifier()
    rfecv = RFECV(estimator=clf_rf_4, step=1, cv=5, scoring='accuracy')  # 5-fold cross-validation
    rfecv = rfecv.fit(trainX,trainY)

    #print('Optimal number of features :', rfecv.n_features_)
    #print('Best features :', trainX.columns[rfecv.support_])

    selectedFeatures = list()

    trainX_selected = rfecv.transform(trainX)
    # print(trainX_selected)

    regressor = LinearRegression()


    regressor.fit(trainX_selected , trainY)

    testX_selected = rfecv.transform(testX)
    preds = regressor.predict(testX_selected)

    return preds

'''

def LRFS(trainX,trainY,testX):

   # print(trainY)
    lr = LinearRegression()
    #lr = LogisticRegression()

    selecteur = RFE(estimator= lr)
    sol = selecteur.fit(trainX,trainY)
    #print(sol.n_features_)
    #print(sol.support_)

    X_new_app = trainX[:,sol.support_]
    #print(X_new_app.shape)
    modele_sel = lr.fit(X_new_app,trainY)

    X_new_test = testX[:,sol.support_]

    preds = modele_sel.predict(X_new_test)

    return preds

'''

def LRFS(trainX,trainY,testX):
    regressor = LinearRegression()
    regressor.fit(trainX, trainY)
    preds = regressor.predict(testX)
    return preds


def LRFS(trainX,trainY,testX):
    print(type(trainY))
    print(trainY.columns)
    regressor = LinearRegression()
    regressor.fit(trainX, trainY)
    preds = regressor.predict(testX)
    return preds
'''