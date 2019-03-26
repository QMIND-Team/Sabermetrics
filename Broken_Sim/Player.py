import Simulator
import warnings
import pandas as pd
from Simulator.Reliever import *
from Simulator.Positional import *
from Simulator.Pitcher import *
from pybaseball import pitching_stats_bref

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Player']

# ignore warnings in code
warnings.simplefilter("ignore")

# calling classes to produce an instance
reliever = Reliever()
pitcher = Pitcher()
positional = Positional()


# class for player (Parent class to Pitcher, Reliever, Positional, and DesignatedHitter)
class Player:
    # initialization of instance variables
    def __init__(self, playerID):
        self.playerID = playerID

    # method to fetch the number of innings pitched by a pitcher in a season
    def inningsPitched(self):
        pitching = pitching_stats_bref(2018)
        pitching_df = pd.DataFrame(pitching)
        pitching_df.set_index("Name", inplace=True)
        pitch_df = pitching_df.loc[self.playerID]
        IP = pitch_df.loc['IP']
        return IP

    # method to distinguish between starting pitchers and relievers
    def position(self):
        # global player_df
        IP = self.inningsPitched()
        if 10 < IP < 60:            # if player has pitched more than 10 innings but less than 60, player is a reliever
            return "Reliever"
            # player_df = reliever.getRelieverStats(self.playerID)
        elif IP > 60:               # if player has pitched more than 60 innings, player is a starting pitcher
            return "Pitcher"
            # player_df = pitcher.getPitcherStats(self.playerID)
        else:                       # if player has pitched less than 10 innings, player is a positional player
            return "Positional"
            # positional(self.playerID)
