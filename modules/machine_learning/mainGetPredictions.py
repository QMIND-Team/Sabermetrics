
import warnings
import modules.machine_learning.help_main as help_main

warnings.filterwarnings("ignore")

import modules.machine_learning.main_advanced_functions as maf

requiredColumns = ["Season","Team",]
allFeatures = ['L', 'SV', 'G_x', 'GS', 'IP', 'SO', 'K/9',
       'BB/9', 'HR/9', 'BABIP_x', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP',
       'WAR_x', 'G_y', 'PA', 'HR', 'R', 'RBI', 'SB', 'BB%', 'K%', 'ISO',
       'BABIP_y', 'AVG', 'OBP', 'SLG', 'wOBA', 'wRC+', 'BsR', 'Off', 'Def',
       'WAR_y']

'''
Example program:
method = "LR"
trainRange = 4
end = 2016
start = 2014
showProcess= 1
toPredictFeatures = ['G_y', 'GS']
'''

def getPredictions(start,end,trainRange,toPredictFeatures,showProcess,method):

    df = help_main.getAll(start-trainRange,end)
    df =  maf.getPredictions(toPredictFeatures,df,method,end,start,showProcess,trainRange)

    return df

