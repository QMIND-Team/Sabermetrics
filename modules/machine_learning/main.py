
import warnings


import modules.machine_learning.help_main as help_main


import modules.machine_learning.main_functions as mf

import modules.machine_learning.advanced_feature_selection as af
warnings.filterwarnings("ignore")

import modules.machine_learning.main_advanced_functions as maf
'''
Methods: 
LR = Linear Regression
SVM = Support Vector Machine 
XGB = XGBOOST 

Programs:
Change value of program to 1 if you  want to execute the program and adjust its parameter values 
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
_____________________________________________CONTROL START__________________________________________________________
'''

#Starting features for the model (currently the best for LR)

testedFeatures = ['G_y', 'GS', 'WAR_x', 'BB%','K/9', 'GB%', 'ERA','xFIP', 'LOB%'] #best combination for LR
requiredColumns = ["Season","Team",]
allFeatures = ['L', 'SV', 'G_x', 'GS', 'IP', 'SO', 'K/9',
       'BB/9', 'HR/9', 'BABIP_x', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP',
       'WAR_x', 'G_y', 'PA', 'HR', 'R', 'RBI', 'SB', 'BB%', 'K%', 'ISO',
       'BABIP_y', 'AVG', 'OBP', 'SLG', 'wOBA', 'wRC+', 'BsR', 'Off', 'Def',
       'WAR_y']


targetFeature = "W"
method = "LR"
#demonstrateModel is very useful for learning about how the model works

# --------------------------------------------Functions Start-----------------------------------------------
#Common Features:
#To do: Rename features to be more consistent and place common features before the if statements

#Train
featureSelection = 0
testSeason = 0
testSeasons = 0
getPredictions =0
advancedPrediction =0
runAdvancedModel =0
advancedFeatureSelection =1

if featureSelection ==1:
    trainRange = 5
    numberOfSeasonsTested = 5
    maximumIterations = 10
    end = 2018
    start = end-trainRange-numberOfSeasonsTested

#Test Season
if testSeason ==1:
    seasonToTest = 2016
    trainRange= 5
    showPreds = 0
    demonstrateModel = 0
    showRMS = 1
    end = seasonToTest
    start = end - trainRange
    demonstrateModel =0
    givePredictions =1
    showPredictions =0

if testSeasons ==1:
    maxSeason = 2018
    numberOfSeasons = 5
    trainRange = 5
    showPreds = 0
    demonstrateModel = 0
    showRMS = 1
    end = maxSeason
    start = end - trainRange-numberOfSeasons
    demonstrateModel = 0
    givePredictions = 1
    showPredictions = 0


if getPredictions ==1:
    trainRange = 5
    end = 2016
    start = end - trainRange
    range = 2
    showProcess= 1
    toPredictFeatures = ['G_y', 'GS']

if advancedPrediction ==1:
    seasonToPredict = 2018
    testRange = 5
    end = seasonToPredict
    start = end - (testRange+1)
    showProcess = 1
    toPredictFeatures = ['OBP', 'G_y', 'FIP', 'K%', 'HR/FB', 'LOB%', 'K/9', 'wRC+', 'GS', 'SB', 'BABIP_x', 'R']


if runAdvancedModel ==1:
    maxSeason = 2018
    testRange = 5
    end = maxSeason
    start = end - (testRange+1)
    showProcess = 1
    toPredictFeatures = ['G_y', 'GS', 'WAR_x', 'BB%','K/9', 'GB%', 'ERA','xFIP', 'LOB%']

    seasonsToTest =4

if advancedFeatureSelection ==1:
    maxSeason = 2018
    testRange = 4#also train range #train ones less than inputted value, more than 5 may cause null values which break the program
    end = maxSeason
    seasonsToTest = 4 #when calculating RMSE and accuracy, it averages the number of seasons entered, more than 5 may cause null values which break the program
    start = end - (testRange+1+seasonsToTest)
    showProcess = 0
    #advancedTestedFeatures = ['OBP', 'G_y', 'FIP', 'K%', 'HR/FB', 'LOB%', 'K/9', 'wRC+', 'GS', 'SB', 'BABIP_x', 'R'] #10.496 RMSE
    #advancedTestedFeatures = ['OBP', 'G_y', 'FIP', 'K%', 'HR/FB', 'LOB%', 'K/9', 'wRC+', 'GS', 'SB', 'BABIP_x', 'R'] #11 RMSE extra advanced

    advancedTestedFeatures = ['G_y']
    advancedToTestFeatures = allFeatures
    for i in advancedTestedFeatures:
        advancedToTestFeatures.remove(i)
    print(advancedToTestFeatures)

# ----------------------------------------------Functions End-----------------------------------------------

'''
_________________________________________________CONTROL END____________________________________________________________

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------'''
requiredColumns.append(targetFeature)
df = help_main.getAll(start,end)
allFeatures = df.columns
toTestFeatures = help_main.getSortedFeatures(testedFeatures,requiredColumns,allFeatures)



if featureSelection == 1:
    mf.featureSelection(df,trainRange,numberOfSeasonsTested,testedFeatures,toTestFeatures,requiredColumns,targetFeature,method)

elif testSeason ==1:
    mf.testSeason(df,targetFeature,testedFeatures,requiredColumns,seasonToTest,trainRange,method,showPreds,showRMS,demonstrateModel,givePredictions,showPredictions)


elif testSeasons ==1:
    mf.testSeasons(df,targetFeature,testedFeatures,requiredColumns,maxSeason,trainRange,method,showPreds,showRMS,demonstrateModel,givePredictions,showPredictions,numberOfSeasons)

elif getPredictions ==1:
    maf.getPredictions(toPredictFeatures,df,method,end,start,showProcess,range)

elif advancedPrediction ==1:
    maf.advancedModel(toPredictFeatures,df,end,start,showProcess,testRange,targetFeature,method,testRange)
elif runAdvancedModel ==1:
    maf.runAdvancedModel(toPredictFeatures, df, end, start, showProcess, testRange, targetFeature, method, seasonsToTest)

elif advancedFeatureSelection==1:
    af.advancedFeatureSelection(df, end, start, testRange, targetFeature, method, seasonsToTest, advancedTestedFeatures,advancedToTestFeatures,showProcess)