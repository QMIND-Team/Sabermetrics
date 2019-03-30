

import warnings



import modules.machine_learning.main_model.help_main as help_main


import modules.machine_learning.advanced_model.main_advanced_functions as maf


import modules.machine_learning.advanced_model.advanced_feature_selection as af
warnings.filterwarnings("ignore")

advancedFeatureSelection =1
runAdvancedModel = 1
#-----------------------------------------------------------------------------------------------------------------


if advancedFeatureSelection ==1:
    maxSeason = 2018
    testRange = 4 #also train range #train ones less than inputted value, more than 5 may cause null values which break the program
    end = maxSeason
    seasonsToTest = 4 #when calculating RMSE and accuracy, it averages the number of seasons entered, more than 5 may cause null values which break the program
    start = end - (testRange+1+seasonsToTest)
    showProcess = 0
    advancedTestedFeatures = ['G_y']
    advancedToTestFeatures = allFeatures
    for i in advancedTestedFeatures:
        advancedToTestFeatures.remove(i)


if runAdvancedModel ==1:
        maxSeason = 2018
        testRange = 5
        end = maxSeason
        start = end - (testRange+1)
        showProcess = 1
        toPredictFeatures = ['G_y','OBP']
        seasonsToTest =5

#-----------------------------------------------------------------------------------------------------------------

requiredColumns.append(targetFeature)
df = help_main.getAll(start, end)
allFeatures = df.columns
toTestFeatures = help_main.getSortedFeatures(testedFeatures, requiredColumns, allFeatures)


if advancedFeatureSelection == 1:
        af.advancedFeatureSelection(df, end, start, testRange, targetFeature, method, seasonsToTest,advancedTestedFeatures, advancedToTestFeatures, showProcess)


elif runAdvancedModel ==1:
    maf.runAdvancedModel(toPredictFeatures, df, end, start, showProcess, testRange, targetFeature, method, seasonsToTest)
