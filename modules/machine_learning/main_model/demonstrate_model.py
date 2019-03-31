import pandas as pd
def printByTeam(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df = df.sort_values(by="Team", ascending=True)
        print(df)



def checkpointOne(trainX,trainY,end):
    print("\n\n-----------------------------Checkpoint One-----------------------------")
    print("The last season is ",end, "and is reserved for validating")
    maxTrainX = trainX["Season"].max()
    minTrainX = trainX["Season"].min()
    minTrainY = trainY["Season"].min()
    maxTrainY= trainY["Season"].max()

    print("The maximum value of trainX should be 2 less than the last season ")
    print("Range of trainX ",minTrainX," to ", maxTrainX)

    print("The maximum value of trainY should be 1 less than the last season ")
    print("Range of trainY ", minTrainY, " to ", maxTrainY, "\n")


def checkpointTwo(trainX,trainY):
    print("\n\n-----------------------------Checkpoint Two-----------------------------")
    print("The target feature from trainY will be added to trainX in the row that v to the previous year for the same team ")
    print("Below are trainX's columns, as you can see \"TargetFeature\"is not including")
    print(trainX.columns)
    print("Below is the full dataframe for trainY")
    print("Notice how it includes the columns Team,Season and the \"TargetFeature\"")
    printByTeam(trainY)

def checkpointThree(trainX):
    print("\n\n-----------------------------Checkpoint Three-----------------------------")
    print("The target feature has now been added to its corresponding row ")
    print("Key columns for the  trainX dataframe will be printed below, notice how for each row the target feature is the same value as the target feature for the team's next season")
    printX = trainX[["targetFeature", "Team", "Season"]]
    printByTeam(printX)


def checkpointFour(trainY):
    print("\n\n-----------------------------Checkpoint Four-----------------------------")
    print("trainY is updated to the \"targetFeature\" column of trainX since the target feature has now been matched ")
    print(trainY)

def checkpointFive(trainX):
    print("\n\n-----------------------------Checkpoint Five-----------------------------")
    print("Non-numeric columns for trainX such as \"Team\" have been dropped.")
    print("trainX columns: ")
    print(trainX.columns)


def checkpointSix(trainX):
    print("\n\n-----------------------------Checkpoint Six-----------------------------")
    print("The target feature has been dropped from trainX to prevent overfitting")
    print("trainX columns: ")
    print(trainX.columns)


def checkpointSeven(trainX):
    print("\n\n-----------------------------Checkpoint Seven-----------------------------")
    print("trainX has been scaled")
   #print(trainX)

def checkpointEight(testX,testY,end):
    print("\n\n-----------------------------Checkpoint Eight-----------------------------")
    print("The last season is ", end, "and is used for validating")
    maxTrainX = testX["Season"].max()
    minTrainX = testX["Season"].min()
    minTrainY = testY["Season"].min()
    maxTrainY = testY["Season"].max()

    print("The maximum value of testX should be 1 less than the last season ")
    print("Range of trainX ", minTrainX, " to ", maxTrainX)
    print("The maximum value of testY should be equal to the last season ")
    print("Range of trainY ", minTrainY, " to ", maxTrainY, "\n")
    print("Both trainX and trainY should have a range of one season ")

def checkpointNine():
    print("\n\n-----------------------------Checkpoint Nine-----------------------------")
    print("The  same process that was used to determine trainX and trainY was used on testX and testY")

def checkpointTen(method,preds):
    print("\n\n-----------------------------Checkpoint Ten-----------------------------")
    if method == "LR":
        newMethod = "Linear Regression"

    elif method == "XGB":
        newMethod = "Extreme Gradient Boosting"
    elif method == "SVM":
        newMethod = 'Support Vector Machine'

    print("Machine Learning Method: ",newMethod)
    print("trainX and trainY were used to fit the data. ")
    print("The fitted model was used to make predictions using testX as the input.")
    print("The predictions are shown below: ")
    print(preds)

def checkpointEleven(showPreds):
    print("\n\n-----------------------------Checkpoint Eleven-----------------------------")
    print("The predictions are organized and combined with other columns to increase readability.")
    print("The result is: ")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(showPreds)

def checkpointTwelve(meanDifference, RMSE):
    print("\n\n-----------------------------Checkpoint Twelve-----------------------------")
    print("The mean error is calculated in two steps:")
    print("1. A column was created by taking the absolute value of the \"targetFeature\" subtracted from the predicted value for each row")
    print("2. The mean of this row was then calculated")
    print("To find the RMSE, was then cacluated by using an imported library from skylearn and compairing testY and  preds")
    print("The average error is ",meanDifference)
    print("The RMSE  is: ",RMSE)
    print("\n\n-----------------------------Done -----------------------------")
