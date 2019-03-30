
import warnings


import modules.machine_learning.main_model.help_main as help_main


import modules.machine_learning.main_model.main_functions as mf

import modules.machine_learning.main_model.predict_2019.modelFor2019 as nextYear

warnings.filterwarnings("ignore")



testedFeatures = ['G_y', 'GS', 'WAR_x', 'BB%','K/9', 'GB%', 'ERA','xFIP', 'LOB%'] #best combination for LR wins


allFeatures = ['L', 'SV', 'G_x', 'GS', 'IP', 'SO', 'K/9',
       'BB/9', 'HR/9', 'BABIP_x', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP',
       'WAR_x', 'G_y', 'PA', 'HR', 'R', 'RBI', 'SB', 'BB%', 'K%', 'ISO',
       'BABIP_y', 'AVG', 'OBP', 'SLG', 'wOBA', 'wRC+', 'BsR', 'Off', 'Def',
       'WAR_y']
requiredColumns = ["Season","Team"]


featureSelection = 0
testSeason = 1
predict2019 = 0

targetFeature = "W"
method = "LR"
trainRange = 4

#contorl start
#------------------------------------------------------------------------------------------------------------------------------------------------
if featureSelection ==1:
    numberOfSeasonsToTest = 4
    print("Determining optimal features for ",targetFeature)

elif testSeason ==1:
    seasonToTest = 2016
    print("Testing",targetFeature,"for",seasonToTest)

elif predict2019 ==1:
    print("Predicting",targetFeature,"for 2019")
#Control end

#----------------------------------------------------------------------------------------------------------------------------------


#Advanced control start
if testSeason ==1:
    showPreds = 1
    trainRange= 4
    demonstrateModel = 0
    showRMS = 1
    end = seasonToTest
    start = end - trainRange
    givePredictions =0
    showPredictions =0



elif predict2019 ==1:
    start = 2018-trainRange
    end = 2018


elif featureSelection ==1:
    maximumIterations = 10
    end = 2018
    start = end-trainRange-numberOfSeasonsToTest

#Advanced control end

#----------------------------------------------------------------------------------------------------------------------------------
requiredColumns.append(targetFeature)
df = help_main.getAll(start, end)
allFeatures = df.columns
toTestFeatures = help_main.getSortedFeatures(testedFeatures, requiredColumns, allFeatures)


if featureSelection == 1:
    mf.featureSelection(df,trainRange,numberOfSeasonsToTest,testedFeatures,toTestFeatures,requiredColumns,targetFeature,method)

elif testSeason ==1:
    mf.testSeason(df,targetFeature,testedFeatures,requiredColumns,seasonToTest,trainRange,method,showPreds,showRMS,demonstrateModel,givePredictions,showPredictions)


elif predict2019 ==1:
    nextYear.model2019(targetFeature, df, start, method)