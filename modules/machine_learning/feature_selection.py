
import random
import warnings
warnings.filterwarnings("ignore")
import modules.machine_learning.model as mod



def getFeatures(df,trainRange,seasonsTested,testedFeatures,toTestFeatures,requiredColumns,finished,target,method):
    random.shuffle(toTestFeatures)
    print("to test features: ")
    print(toTestFeatures)
    while(finished == 0):
        change = 0
        testAgain = list()
        firstTest = list()
        firstTest.extend(testedFeatures)
        firstTest.extend(requiredColumns)
        dfTest = df[firstTest]

        bestAccurracy, bestAvgRMS = mod.runModel(dfTest, trainRange, seasonsTested, target,method,0,1)

        print("The starting accuracy is: ",bestAccurracy)
        print("The starting average RMS is ",bestAvgRMS)
        print("")
        print("")

        #--------------------------------------------
        #print(toTestFeatures)

        for testing in toTestFeatures:
            print("#---------------------------------------------------------")

            print("Adding: ", testing)

            testingFeatures = list()
            testingFeatures.extend(testedFeatures)
            testingFeatures.extend([testing])

            testingFeatures.extend(requiredColumns)

            print("Testing features: ")
            print(testingFeatures)
            testDf = df[testingFeatures]
            MDAVG,avgRMS = mod.runModel(testDf,trainRange,seasonsTested,target,method,0,1)

            print("After testing: ",testing," the accuracy is ",MDAVG)
            print("After testing: ",testing," the average RMS is ",avgRMS,"\n")
            if(avgRMS-bestAvgRMS<3):
                testAgain.extend([testing])



        print("The features that will be retested are: ",testAgain)
        print("The final features are: ",testedFeatures)
        print("The final accuracy is: ",bestAccurracy)
        print("The RMSE is: ",bestAvgRMS)

       # print(rmsDictionary)
        if (change>0):
            getFeatures(df, trainRange, 5, 5, testAgain, requiredColumns, 0)

        else:
            finished =1
            print("Complete")
            return testedFeatures,testAgain

def removeFeatures(df,trainRange,seasonsTested,testedFeatures,requiredColumns,target):
    print("Now removing Columns ")
    random.shuffle(testedFeatures)
    print(testedFeatures)

    removed = list()
    #--------------------------------------------
    firstTest = list()
    firstTest.extend(testedFeatures)
    firstTest.extend(requiredColumns)
    dfTest = df[firstTest]

    bestAccurracy, bestAvgRMS = mod.runModel(dfTest, trainRange, seasonsTested, target,method,0,1)

    print("The starting accuracy is: ",bestAccurracy)
    print("The starting average RMS is ",bestAvgRMS,"\n\n")


    #--------------------------------------------
    for testing in testedFeatures:
        tempTest = list()

        print("#---------------------------------------------------------")
        print("Removing features: ",testing," from ",testedFeatures)

        testedFeatures.remove(testing)
        tempTest.extend(testedFeatures)
        tempTest.extend(requiredColumns)
        testDf = df[tempTest]

        MDAVG, avgRMS = mod.runModel(testDf, trainRange, seasonsTested, target,method,0,1)

        print("After testing: ", testing, " the accuracy is ", MDAVG)
        print("After testing: ", testing, " the average RMS is ", avgRMS)

        if(avgRMS<bestAvgRMS):
            print(testing, " was removed ")
            removed.extend([testing])
            bestAvgRMS = avgRMS
            bestAccurracy = MDAVG
        else:
            print(testing," stays")
            testedFeatures.extend([testing])
    print("The final features are: ", testedFeatures)
    print("The final accuracy is: ", bestAccurracy)
    print("The RMSE is: ", bestAvgRMS)


    return testedFeatures,removed
