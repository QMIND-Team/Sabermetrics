import Simulator
import warnings
from Simulator.Game import *
from Simulator.Bases import *

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Batter']

# ignore warnings in code
warnings.simplefilter("ignore")

# calling classes to produce an instance
game = Game()
bases = Bases()


# class for all behaviors/stats of batters
class Batter:
    # initialization of instance variables
    def __init__(self):
        self.strikes = 0
        self.balls = 0
        self.hits = 0
        self.walks = 0

    # method for behavior of a strike
    def strike(self):
        self.strikes = self.strikes + 1     # add one to strike count
        if self.strikes == 3:               # if batter has 3 strikes, batter is out
            game.out()
            self.nextBatter()               # calls function to get stats on the next batter

    # method for behavior of a ball
    def ball(self):
        self.balls = self.balls + 1         # add one to ball count
        if self.balls == 4:                 # if batter gets 4 balls
            self.walks = self.walks + 1
            self.single()                   # walk to first
            self.nextBatter()               # calls function to get the next batters stats

    # method to fetch next batter statistics
    def nextBatter(self):
        self.strikes = 0                    # resets strike/ball count to zero
        self.balls = 0
        pass                                # get next batters statistics

    # method printing out the current batting record of player at bat
    def battingRecord(self):
        print("Batting record : {} strikes, and {} balls".format(self.strikes, self.balls))

    # method for behavior of a single hit
    def single(self):
        self.hits = self.hits + 1
        self.nextBatter()
        if bases.basesLoaded:               # bases will stay loaded and one run will be scored
            game.runScored()
        else:
            if bases.third:
                if not bases.second:        # if second base is empty, third base will become empty
                    bases.third = False
                game.runScored()            # run scored and the player from second will occupy third if true
            if bases.second:
                if not bases.first:         # if first base is empty, second base will become empty
                    bases.second = False
                bases.third = True          # otherwise, it will be occupied by the player that was on first
            if bases.first:                 # first will stay occupied by the player who was batting
                bases.second = True
        bases.first = True                  # player guaranteed to be on first

    # method for behavior of a double hit
    def double(self):
        self.hits = self.hits + 1
        self.nextBatter()
        if bases.basesLoaded:               # if bases loaded, two players will score and first will become empty
            bases.first = False
            game.runScored()
            game.runScored()
        else:
            if bases.third:
                if not bases.first:         # if first is empty, third will become empty
                    bases.third = False
                game.runScored()            # run scored and the player from first will occupy third if true
            if bases.first:                 # first will no longer be occupied
                bases.first = False
                bases.third = True
            if bases.second:                # second base will stay occupied by player who was batting
                game.runScored()
        bases.second = True                 # player guaranteed to be on second

    # method for behavior of a triple hit
    def triple(self):
        self.hits = self.hits + 1
        self.nextBatter()
        if bases.basesLoaded:               # all players on base will score a run
            bases.first = False
            bases.second = False
            bases.Third = False
            game.runScored()
            game.runScored()
            game.runScored()
        else:
            if bases.third:                 # run scored by occupant, stays occupied by the player who was batting
                game.runScored()
            if bases.first:                 # player on first will have scored
                bases.first = False
                game.runScored()
            if bases.second:                # player on second will have scored
                bases.second = False
                game.runScored()
        bases.third = True                  # player guaranteed to be on third

    # method for behavior of a home run hit
    def homeRun(self):
        self.hits = self.hits + 1
        self.nextBatter()
        if bases.basesLoaded:               # all players on base and batter will score a run
            bases.first = False
            bases.second = False
            bases.third = False
            game.runScored()
            game.runScored()
            game.runScored()
            game.runScored()
        else:
            if bases.first:                 # first becomes empty and a run is scored
                bases.first = False
                game.runScored()
            if bases.second:                # second becomes empty and a run is scored
                bases.second = False
                game.runScored()
            if bases.third:                 # third becomes empty and a run is scored
                bases.third = False
                game.runScored()
            game.runScored()                # run scored by batter
