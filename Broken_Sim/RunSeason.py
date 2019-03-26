import Simulator
import warnings
from random import uniform
from Simulator.TeamName import *
from Simulator.Season import *
from Simulator.Game import *
from Simulator.Batter import *
from Simulator.Bases import *
from Simulator import RunExpectancy

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['runSeason']

# ignore warnings in code
# warnings.simplefilter("ignore")

# calling classes to produce an instance
season = Season(TeamName.name)
game = Game()
batter = Batter()
bases = Bases()


# run the Season
def runSeason():
    while season.games < 163:
        swing = uniform(0.0, 1.0)
        if swing <= 0.635:  # batters swing at 63.5% of all pitches
            strikeZone = uniform(0.0, 1.0)
            if strikeZone <= 0.45:  # 45% of all pitches are inside the strike zone
                hit = uniform(0.0, 1.0)
                if hit <= 0.8075:  # 80.75% of swings in strike zone will hit
                    expectancy = RunExpectancy.getRunExpectancy()
                    runChance = uniform(0.0, 3.0)
                    if runChance <= expectancy:
                        game.runScored()
                    else:
                        game.out()
                else:  # swing and miss, resulting in a strike
                    batter.strike()
            else:  # not in strike zone but still swing, results in strike
                batter.strike()
        else:  # Batter did not swing and not in strike zone, results in a ball
            batter.ball()
        if Bases.first:
            throwOut = uniform(0.0, 1.0)
            if throwOut <= 0.3:
                game.out()
                Bases.first = False
            else:
                pass
        elif Bases.second:
            throwOut = uniform(0.0, 1.0)
            if throwOut <= 0.3:
                game.out()
                Bases.second = False
            else:
                pass
        elif Bases.third:
            throwOut = uniform(0.0, 1.0)
            if throwOut <= 0.3:
                game.out()
                Bases.third = False
            else:
                pass
