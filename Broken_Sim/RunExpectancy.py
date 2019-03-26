import Simulator
import warnings
from Simulator.Game import *
from Simulator.Bases import *

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['getRunExpectancy']

# ignore warnings in code
warnings.simplefilter("ignore")

# calling classes to produce an instance
game = Game()
bases = Bases()


# get the run expectancy based on the state of runners on base compared to the number of outs
def getRunExpectancy():
    global RE
    if game.outs == 0:
        if not bases.first and not bases.second and not bases.third:    # No runners on base
            RE = 0.461                                                  # Run Expectancy
        elif bases.first and not bases.second and not bases.third:      # Runner only on first base
            RE = 0.831                                                  # Run Expectancy
        elif not bases.first and bases.second and not bases.third:      # Runner only on second base
            RE = 1.068                                                  # Run Expectancy
        elif not bases.first and not bases.second and bases.third:      # Runner only on third base
            RE = 1.426                                                  # Run Expectancy
        elif bases.first and bases.second and not bases.third:          # Runners on first and second
            RE = 1.373                                                  # Run Expectancy
        elif bases.first and not bases.second and bases.third:          # Runners on first and third
            RE = 1.798                                                  # Run Expectancy
        elif not bases.first and bases.second and bases.third:          # Runners on second and third
            RE = 1.920                                                  # Run Expectancy
        elif bases.basesLoaded:                                         # bases Loaded
            RE = 2.282                                                  # Run Expectancy
    elif game.outs == 1:
        if not bases.first and not bases.second and not bases.third:    # No runners on base
            RE = 0.243                                                  # Run Expectancy
        elif bases.first and not bases.second and not bases.third:      # Runner only on first base
            RE = 0.489                                                  # Run Expectancy
        elif not bases.first and bases.second and not bases.third:      # Runner only on second base
            RE = 0.644                                                  # Run Expectancy
        elif not bases.first and not bases.second and bases.third:      # Runner only on third base
            RE = 0.865                                                  # Run Expectancy
        elif bases.first and bases.second and not bases.third:          # Runners on first and second
            RE = 0.908                                                  # Run Expectancy
        elif bases.first and not bases.second and bases.third:          # Runners on first and third
            RE = 1.140                                                  # Run Expectancy
        elif not bases.first and bases.second and bases.third:          # Runners on second and third
            RE = 1.352                                                  # Run Expectancy
        elif bases.basesLoaded:                                         # bases Loaded
            RE = 1.520                                                  # Run Expectancy
    elif game.outs == 2:
        if not bases.first and not bases.second and not bases.third:    # No runners on base
            RE = 0.095                                                  # Run Expectancy
        elif bases.first and not bases.second and not bases.third:      # Runner only on first base
            RE = 0.214                                                  # Run Expectancy
        elif not bases.first and bases.second and not bases.third:      # Runner only on second base
            RE = 0.305                                                  # Run Expectancy
        elif not bases.first and not bases.second and bases.third:      # Runner only on third base
            RE = 0.413                                                  # Run Expectancy
        elif bases.first and bases.second and not bases.third:          # Runners on first and second
            RE = 0.343                                                  # Run Expectancy
        elif bases.first and not bases.second and bases.third:          # Runners on first and third
            RE = 0.471                                                  # Run Expectancy
        elif not bases.first and bases.second and bases.third:          # Runners on second and third
            RE = 0.570                                                  # Run Expectancy
        elif bases.basesLoaded:                                         # bases Loaded
            RE = 0.736                                                  # Run Expectancy
    return RE
