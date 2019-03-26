import Simulator
import warnings
import pandas as pd
from Simulator import Player
from pybaseball import batting_stats_bref

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['DesignatedHitter']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for designated hitters (child class of Player)
class DesignatedHitter(Player):
    def __init__(self):
        super(DesignatedHitter).__init__()

    # method to fetch batter statistics, returning a data frame
    def getBatterStats(self):
        batter = batting_stats_bref(2018)
        batter_df = pd.DataFrame(batter)
        batter_df.set_index("Name", inplace=True)
        player_df = batter_df.loc[self.playerID]
        return player_df
