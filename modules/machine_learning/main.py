
import warnings


import modules.machine_learning.help_main as help_main


import modules.machine_learning.main_functions as mf

warnings.filterwarnings("ignore")


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
testedFeatures = ['G_y', 'GS', 'WAR_x', 'BB%', 'K/9', 'GB%', 'ERA', 'xFIP', 'LOB%'] #best combination for LR
requiredColumns = ["Season","Team"]

target = "W"
method = "LR"
#demonstrateModel is very useful for learning about how the model works

# --------------------------------------------Functions Start-----------------------------------------------
#Train
featureSelection = 0
if featureSelection ==1:
    trainRange = 5
    numberOfSeasonsTested = 5
    maximumIterations = 10
    end = 2018
    start = end-trainRange-numberOfSeasonsTested

#Test Season
testSeason = 1
if testSeason ==1:
    seasonToTest = 2016
    trainRange= 5
    showPreds = 0
    demonstrateModel = 1
    showRMS = 0
    end = seasonToTest
    start = end - trainRange

#Test Seasons
testSeasons = 0
if testSeasons == 1:
    lastSeason = 2018
    trainRange= 5
    showPreds = 0
    showRMS = 1
    demonstrateModel = 0
    numberOfSeasons = 5
    end = lastSeason
    start = lastSeason -trainRange - numberOfSeasons



# ----------------------------------------------Functions End-----------------------------------------------


'''
_________________________________________________CONTROL END____________________________________________________________

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------'''
requiredColumns.append(target)
df = help_main.getAll(start,end)
allFeatures = df.columns
toTestFeatures = help_main.getSortedFeatures(testedFeatures,requiredColumns,allFeatures)



if featureSelection == 1:
    mf.featureSelection(df,trainRange,numberOfSeasonsTested,testedFeatures,toTestFeatures,requiredColumns,target,method)

elif testSeason ==1:
    mf.testSeason(df,target,testedFeatures,requiredColumns,seasonToTest,trainRange,method,showPreds,showRMS,demonstrateModel)

elif testSeasons ==1:
    mf.testSeasons(df,target,testedFeatures,requiredColumns,trainRange,method,showPreds,showRMS,numberOfSeasons,lastSeason,demonstrateModel)

