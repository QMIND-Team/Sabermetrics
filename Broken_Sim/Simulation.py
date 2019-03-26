# importing libraries used throughout simulator
import Simulator
import warnings
import pandas as pd
from Simulator.TeamName import *
from Simulator.Season import *

Simulator.__all__ = ['setTeamName', 'name']

# ignore warnings in code
# warnings.simplefilter("ignore")

pd.set_option("display.max_rows", 162)
pd.set_option("display.max_columns", 9)


def setTeamName(teamName):
    name = TeamName(teamName)
    return name


name = setTeamName("Yankees")   # input name of specific team of interest

# initializing objects
season = Season(name)

season.data_df.set_index("Game", inplace=True, drop=True)
print(season.data_df)
