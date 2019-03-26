import Simulator
import warnings
from Simulator import TeamsPlaying

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Home']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for home games (child class of Team)
class Home(TeamsPlaying):
    def __init__(self):
        super(Home).__init__()

    # accessor to return stadium adjustment for home team
    def getStadiumAdjust(self):
        pass
