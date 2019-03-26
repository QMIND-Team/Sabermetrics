import Simulator
import warnings
import pandas as pd
from Simulator.Game import *
from Simulator.TeamsPlaying import *
from Simulator import MLB_2019_Schedule as MLB

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['Season']

# ignore warnings in code
# warnings.simplefilter("ignore")

# calling classes to produce an instance
game = Game()


# class for season
class Season:
    # initialization of class instance variables
    def __init__(self, teamName):
        self.games = 1
        self.teamName = teamName
        self.data_df = pd.DataFrame(columns={'Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team',
                                             'League'})
        self.hardCoding = False  # set to true if user wishes to hard code games

    # declaring accessor for teamName instance attribute
    def getTeamName(self):
        return self.teamName

    # method to run a seasons worth of games for any given team
    def playSeason(self):
        schedule = MLB.getTeamSchedule(self.teamName)               # fetching season schedule for a given team
        home = MLB.homeOrAway(schedule)                             # check which team is at home for each game
        games = MLB.checkFirstBit(schedule)                         # cleaning season schedule
        opposingTeam = iter(games)                                  # declare iterator for games in the season
        gamesPlayed = 0
        teams_df = pd.DataFrame(columns={"Home Team", "Away Team", "League"})   # create a DataFrame to me merged into output
        while gamesPlayed <= 162:
            try:
                current = next(opposingTeam)
                if home[gamesPlayed] == "True":                     # arrange teams in 'Home Team', 'Away Team' columns
                    teams_df = teams_df.append({"Home Team": self.teamName, "Away Team": MLB.toName(current),
                                                "League": TeamsPlaying(self.teamName, MLB.toName(current)).gameLeague()},
                                               ignore_index=True)
                elif home[gamesPlayed] == "False":
                    teams_df = teams_df.append({"Home Team": MLB.toName(current), "Away Team": self.teamName,
                                                "League": TeamsPlaying(MLB.toName(current), self.teamName).gameLeague()},
                                               ignore_index=True)
                gamesPlayed = gamesPlayed + 1
            except StopIteration:
                break
        return teams_df

    def nextGame(self):
        if self.hardCoding:
            self.games = self.games + 1
        else:
            teams_df = self.playSeason()  # fetching Data Frame of season outcomes
            self.data_df = self.data_df[['Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team',
                                         'League']]
            self.data_df = self.data_df.append({'Game': self.games, 'Home Team Score': game.score[0],
                                                'Away Team Score': game.score[1]}, ignore_index=True)
            self.data_df.update(teams_df)  # update the Data frame with data from season outcomes
            self.games = self.games + 1
