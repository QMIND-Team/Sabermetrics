import Simulator
import warnings
from Simulator import TeamsPlaying

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Away']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for away games (child class of Team)
class Away(TeamsPlaying):
    def __init__(self):
        super(Away).__init__()

    # accessor to return stadium adjustment for away team
    def getStadiumAdjust(self):
        pass
