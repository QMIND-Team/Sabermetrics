import Simulator
import warnings

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Bases']

# ignore warnings in code
warnings.simplefilter("ignore")


# class to track base status
class Bases:
    # initialization of instance variables
    def __init__(self):
        self.first = False
        self.second = False
        self.third = False
        self.basesLoaded = False

    # method to simulate loaded bases
    def loadedBases(self):                  # if there are players on every base, bases are loaded
        if self.first and self.second and self.third:
            self.basesLoaded = True
        else:                               # otherwise bases are not loaded
            self.basesLoaded = False

    # method to output which bases are occupied
    def playerOn(self):
        self.loadedBases()                  # check if bases are loaded
        if not self.basesLoaded:            # if they aren't
            if self.first:                  # check all individual bases to see if they are occupied
                print("Player on first")
            else:
                print("First is empty")
            if self.second:
                print("Player on Second")
            else:
                print("Second is empty")
            if self.third:
                print("Player on third")
            else:
                print("Third is empty")
        else:                               # otherwise, all bases are loaded
            print("Bases Loaded")
        print("\n")
