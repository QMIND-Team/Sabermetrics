import Simulator
import warnings
import pandas as pd
from Simulator import Player
from pybaseball import pitching_stats_bref

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Pitcher']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for pitchers (child class of Player)
class Pitcher(Player):
    def __init__(self):
        super(Pitcher).__init__()

    # method to fetch starting pitcher statistics, returning data frame
    def getPitcherStats(self):
        pitcher = pitching_stats_bref(2018)
        pitcher_df = pd.DataFrame(pitcher)
        pitcher_df.set_index("Name", inplace=True)
        player_df = pitcher_df.loc[self.playerID]
        return player_df
