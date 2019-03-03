
import modules.machine_learning.main_functions as mf
import modules.machine_learning.main_advanced_functions as maf
import random



def advancedFeatureAdder(df ,end ,start ,testRange ,targetFeature ,method ,seasonsToTest ,testedFeatures
                         ,toTestFeatures ,showProcess):

    random.shuffle(toTestFeatures)
    print("Potential new features to be added to tested Features ")
    print(toTestFeatures)
    print("Current Tested Features: ")
    print(testedFeatures)
    finished =0
    while (finished == 0):
        change = 0
        testAgain = list()
        firstTest = list()
        print("Getting the starting RMSE")
        bestAccurracy, bestAvgRMSE = maf.runAdvancedModel(testedFeatures, df, end, start, showProcess, testRange,
                                                      targetFeature, method, seasonsToTest)

        print("The starting accuracy is: ", bestAccurracy)
        print("The starting average RMSE is ", bestAvgRMSE)
        print("\n")

        # --------------------------------------------
        # print(toTestFeatures)

        for testing in toTestFeatures:
            print("#---------------------------------------------------------")

            print("Adding: ", testing)

            testingFeatures = list()
            testingFeatures.extend(testedFeatures)
            testingFeatures.extend([testing])

            print("Testing features: ")
            print(testingFeatures)
            MDAVG, avgRMSE = maf.runAdvancedModel(testingFeatures, df, end, start, showProcess, testRange, targetFeature,
                                              method, seasonsToTest)
            if (avgRMSE < bestAvgRMSE):
                testedFeatures.extend([testing])
                print(testing, " has been added to tested features")
                change = change + 1
                bestAvgRMSE = avgRMSE
                bestAccurracy = MDAVG

            else:
                print(testing," has not been added")
                testAgain.extend([testing])

            print("After testing: ", testing, " the accuracy is ", MDAVG)
            print("After testing: ", testing, " the average RMS is ", avgRMSE, "\n")

        print("The features that will be retested are: ", testAgain)
        print("The final features are: ", testedFeatures)
        print("The final accuracy is: ", bestAccurracy)
        print("The RMSE is: ", bestAvgRMSE)
        if change == 0:
            finished = 1

    return testedFeatures, testAgain


def advancedFeatureRemover(df, end, start, testRange, targetFeature, method, seasonsToTest, testedFeatures, showProcess):
    random.shuffle(testedFeatures)
    print("Removing  Features from testedFeatures ")
    print(testedFeatures)
    finished = 0
    removedFeatures = list()
    while (finished == 0):
        change = 0
        testAgain = list()

        bestAccurracy, bestAvgRMSE = maf.runAdvancedModel(testedFeatures, df, end, start, showProcess, testRange,
                                                      targetFeature, method, seasonsToTest)

        print("The starting accuracy is: ", bestAccurracy)
        print("The starting average RMSE is ", bestAvgRMSE)
        print("\n")

        # --------------------------------------------
        # print(toTestFeatures)
        toTestFeatures = testedFeatures
        for testing in toTestFeatures:
            print("#---------------------------------------------------------")

            print("removing: ", testing)

            testedFeatures.remove(testing)

            print("Testing features: ")
            print(testedFeatures)
            MDAVG, avgRMSE = maf.runAdvancedModel(testedFeatures, df, end, start, showProcess, testRange, targetFeature,
                                              method, seasonsToTest)

            if (avgRMSE < bestAvgRMSE):
                print(testing, " has been removed from tested features")
                change = change + 1
                bestAvgRMSE = avgRMSE
                bestAccurracy = MDAVG
                removedFeatures.extend([testing])

            else:
                testedFeatures.extend([testing])
                print(testing, "remains in tested features")
            print("After testing: ", testing, " the accuracy is ", MDAVG)
            print("After testing: ", testing, " the average RMSE is ", avgRMSE, "\n")

        print("The features that will be retested are: ", testAgain)
        print("The final features are: ", testedFeatures)
        print("The final accuracy is: ", bestAccurracy)
        print("The RMSE is: ", bestAvgRMSE)
        if change == 0:
            finished = 1

    return testedFeatures, removedFeatures





def advancedFeatureSelection(df ,end ,start ,testRange ,targetFeature ,method ,seasonsToTest ,testedFeatures,toTestFeatures ,showProcess):

    for i in range(5):


        testedFeatures, toTestFeatures = advancedFeatureAdder(df, end, start, testRange, targetFeature, method, seasonsToTest, testedFeatures, toTestFeatures,showProcess)
        print("###########################################################")
        testedFeatures, removed = advancedFeatureRemover(df, end, start, testRange, targetFeature, method,seasonsToTest, testedFeatures, showProcess)
        toTestFeatures.extend(removed)



    print("Final Features: ",testedFeatures)
