import Simulator
import warnings
import pandas as pd
from Simulator import Player
from pybaseball import pitching_stats_bref

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Reliever']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for relievers (child class of Player)
class Reliever(Player):
    def __init__(self):
        super(Reliever).__init__()

    # method to fetch reliever statistics, returning data frame
    def getRelieverStats(self):
        reliever = pitching_stats_bref(2018)
        reliever_df = pd.DataFrame(reliever)
        reliever_df.set_index("Name", inplace=True)
        player_df = reliever_df.loc[self.playerID]
        return player_df
