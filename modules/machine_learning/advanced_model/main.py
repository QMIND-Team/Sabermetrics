
import warnings

import modules.machine_learning.main_model.help_main as help_main

warnings.filterwarnings("ignore")

import modules.machine_learning.advanced_model.main_advanced_functions as maf
'''
Methods: 
LR = Linear Regression
SVM = Support Vector Machine 
XGB = XGBOOST 


---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
_____________________________________________CONTROL START_________________________________________
'''

#Starting features for the model (currently the best for LR)

#testedFeatures = ['G_y', 'GS', 'WAR_x', 'BB%','K/9', 'GB%', 'ERA','xFIP', 'LOB%'] #best combination for LR
testedFeatures =  ['L']
requiredColumns = ["Season","Team",]
allFeatures = ['L', 'SV', 'G_x', 'GS', 'IP', 'SO', 'K/9',
       'BB/9', 'HR/9', 'BABIP_x', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP',
       'WAR_x', 'G_y', 'PA', 'HR', 'R', 'RBI', 'SB', 'BB%', 'K%', 'ISO',
       'BABIP_y', 'AVG', 'OBP', 'SLG', 'wOBA', 'wRC+', 'BsR', 'Off', 'Def',
       'WAR_y']


targetFeature = "W"
method = "LR"

# --------------------------------------------Functions Start-----------------------------------------------

#Train
advancedModel = 1

if advancedModel ==1:
    seasonToPredict = 2016
    testRange = 4
    end = seasonToPredict
    start = end - (testRange*3)
    showProcess = 1
    #features = ['G_y', 'OBP', 'IP', 'WAR_x', 'SB', 'AVG', 'HR/FB', 'K%', 'LOB%', 'xFIP', 'BB/9', 'Def', 'ERA', 'SLG', 'BABIP_x', 'PA', 'SV', 'R', 'Off', 'WAR_y', 'HR/9']
    features = ['G_y'] #quick model



'''
_________________________________________________CONTROL END_______________________________________

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------'''
requiredColumns.append(targetFeature)
df = help_main.getAll(start, end)
allFeatures = df.columns
toTestFeatures = help_main.getSortedFeatures(testedFeatures, requiredColumns, allFeatures)



if advancedModel ==1:
    maf.advancedModel(features,df,end,start,showProcess,testRange,targetFeature,method,testRange)
