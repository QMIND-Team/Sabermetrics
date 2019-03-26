import Simulator
import warnings
import pandas as pd
from pybaseball import batting_stats_bref
from pybaseball import pitching_stats_bref

# import Machine Learning Algorithm to fetch predicted stats
# from modules.machine_learning import mainGetPredictions as ml

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Team']

# ignore warnings in code
warnings.simplefilter("ignore")


# class for Teams
class Team:
    # initialization of instance variables
    def __init__(self, teamName, teamCity, league):
        self.team = teamCity
        self.league = league
        self.teamName = teamName

    # method to fetch predicted team stats from MLM
    '''def getPredictedStats(self, start, end, trainRange, toPredictFeatures, showProcess, method):
        predictedStats = ml.getPredictions(start, end, trainRange, toPredictFeatures, showProcess, method)
        return predictedStats'''

    # method to fetch batting roster of a given team
    def getBattingRoster(self):
        batting = batting_stats_bref(2018)
        batting_df = pd.DataFrame(batting)
        batting_df.set_index("Tm", inplace=True)
        homeBat_df = batting_df.loc[self.team]
        return homeBat_df

    # method to fetch pitching roster of a given team
    def getPitchingRoster(self):
        pitching = pitching_stats_bref(2018)
        pitching_df = pd.DataFrame(pitching)
        pitching_df.set_index("Tm", inplace=True)
        homePitch_df = pitching_df.loc[self.team]
        return homePitch_df

    # accessor to return league team plays in
    def getLeague(self):
        league = self.league
        return league

    # accessor to return the name of the team
    def getTeamName(self):
        teamName = self.teamName
        return teamName
