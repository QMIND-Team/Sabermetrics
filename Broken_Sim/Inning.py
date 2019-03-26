import Simulator
import warnings
from Simulator.Game import *
from Simulator.Bases import *

from Simulator.Game import Game

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Inning']

# ignore warnings in code
# warnings.simplefilter("ignore")

# calling classes to produce an instance
game = Game()
bases = Bases()


# class for innings (child class of game)
class Inning(game):
    def __init__(self):
        super(Inning).__init__()

    # method to switch between top and bottom of inning
    def inningSwitch(self):                 # sets outs back to zero and switches between top and bottom of inning
        bases.first = False
        bases.second = False
        bases.third = False
        if self.top:
            self.outs = 0
            self.bottomOf()
        else:
            self.outs = 0
            self.topOf()

    # mutator to change the status of the inning (top or bottom of the inning)
    def topOf(self):                        # if top of inning, set top to true
        self.top = True

    # mutator to change the status of the inning (top or bottom of the inning)
    def bottomOf(self):                     # if bottom of inning, sets top to false
        self.top = False
