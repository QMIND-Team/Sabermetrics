import Simulator
import warnings

Simulator.__all__ = ['TeamName']

warnings.simplefilter("ignore")


class TeamName:
    def __init__(self, name):
        self.name = name

    def getTeamName(self):
        return self.name
