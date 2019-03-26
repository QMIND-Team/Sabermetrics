import Simulator
import warnings
import pandas as pd
from Simulator.Season import *
from Simulator.Inning import *
from Simulator.Batter import *
from Simulator.Simulation import *
from Simulator.TeamName import *

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Game', 'columnNames']

# ignore warnings in code
# warnings.simplefilter("ignore")

# Data Frame for box score output
columnNames = ["Inning", "Home Score", "Away Score", "Hits", "Walks"]

# calling classes to produce an instance
teamName = TeamName(name)
season = Season(teamName.name)
inning = Inning()
batter = Batter()


# class for game (parent class of inning)
class Game:
    # initialization of class instance variables
    def __init__(self):
        self.inning = 1
        self.outs = 0
        self.score = [0, 0]
        self.top = False
        self.runsTop = 0
        self.runsBottom = 0
        # Data Frame headings for a hardcoded game
        self.game_df = pd.DataFrame(columns=columnNames)

    # initializing accessor to get the state of the inning (top or bottom)
    def getTop(self):
        return self.top

    # initializing accessor to get the number of outs in the inning
    def getOuts(self):
        return self.outs

    # method for adding runs scored for each team
    def runScored(self):
        if self.top:                        # if top of the inning points awarded to the team of index zero
            self.score[1] = self.score[1] + 1
            self.runsTop = self.runsTop + 1
        else:                               # points awarded to team of index one in the bottom of innings
            self.score[0] = self.score[0] + 1
            self.runsBottom = self.runsBottom + 1
        batter.nextBatter()

    # method for behavior of an out in the game
    def out(self):
        batter.nextBatter()
        self.outs = self.outs + 1           # add one to the out count
        if self.outs == 3:                  # at three outs switch the inning, resetting outs to zero
            self.outs = 0
            inning.inningSwitch()
            if not self.top:                # if its the bottom of the inning, start next inning
                self.game_df = self.inputData(self.game_df)
                self.runsTop = 0
                self.runsBottom = 0
                Batter.hits = 0
                Batter.walks = 0
                self.inning = self.inning + 1
        if self.inning >= 10 and self.score[0] != self.score[1]:        # if 10 innings reached and not tied
            season.nextGame()                                           # game ends, go to next game
            self.endGame()
        elif self.inning == 10 and self.score[0] == self.score[1]:      # otherwise, keep going until one team wins
            pass

    # method to reset the game to starting parameters
    def endGame(self):
        self.inning = 1
        self.outs = 0
        self.score = [0, 0]
        self.top = False

    # method to update the data frame of events occurring in the hard coded game
    def inputData(self, dataFrame):
        walks = abs(batter.walks)
        hits = batter.hits - walks
        dataFrame = dataFrame[["Inning", "Home Score", "Away Score", "Hits", "Walks"]]
        dataFrame = dataFrame.append({"Inning": self.inning, "Home Score": self.runsTop, "Away Score": self.runsBottom,
                                      "Hits": hits, "Walks": walks}, ignore_index=True)
        return dataFrame