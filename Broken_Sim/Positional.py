import Simulator
import warnings
from Simulator import Player

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Positional']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for positional player (child class of Player)
class Positional(Player):
    def __init__(self):
        super(Positional).__init__()

