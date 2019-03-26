import Simulator
import warnings
from Simulator.TeamDeclaration import *

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['TeamsPlaying']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for teams playing in a particular game (parent class to Home and Away)
class TeamsPlaying:
    # initialization of instance variables
    def __init__(self, homeTeam, awayTeam):
        self.home = homeTeam
        self.away = awayTeam

    # accessor to return the home team
    def getHomeTeam(self):
        return self.home

    # accessor to return the away team
    def getAwayTeam(self):
        return self.away

    # method to return the league in which a game falls under (based on the individual leagues of teams playing
    def gameLeague(self):
        homeLeague = ""
        awayLeague = ""
        for team in range(len(NL)):                     # iterate through NL league
            if self.home == NL[team].getTeamName():     # if home team is in NL, set homeLeague to NL
                homeLeague = NL[team].getLeague()
            if self.away == NL[team].getTeamName():     # if away team is in NL, set awayLeague to NL
                awayLeague = NL[team].getLeague()
        for team in range(len(AL)):                     # iterate through AL league
            if self.home == AL[team].getTeamName():     # if home team is in AL, set homeLeague to AL
                homeLeague = AL[team].getLeague()
            if self.away == AL[team].getTeamName():     # if away team is in AL, set awayLeague to AL
                awayLeague = AL[team].getLeague()
        if homeLeague == "MLB-NL" and awayLeague == "MLB-NL":   # if both teams are in NL, game league is NL
            league = "MLB-NL"
        elif homeLeague == "MLB-AL" and awayLeague == "MLB-AL":  # if both teams are in AL, game league is AL
            league = "MLB-AL"
        else:                               # if both teams are in different leagues, game league is Inter-league
            league = "Inter-League"
        return league
