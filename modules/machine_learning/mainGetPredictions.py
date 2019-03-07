
import warnings
import modules.machine_learning.help_main as help_main

warnings.filterwarnings("ignore")

import modules.machine_learning.main_advanced_functions as maf


#Example program:
method = "LR"
trainRange = 4
end = 2016
start = 2014
showProcess= 1
toPredictFeatures = ['G_y', 'GS']


def getPredictions(start,end,trainRange,toPredictFeatures,showProcess,method):

    df = help_main.getAll(start-trainRange,end)
    df =  maf.getPredictions(toPredictFeatures,df,method,end,start,showProcess,trainRange)

    return df

f = getPredictions(start,end,trainRange,toPredictFeatures,showProcess,method)

print(f.head())