from random import uniform
# import simpy as sp
import pandas as pd
import numpy as np

from pybaseball import pitching_stats_bref
from pybaseball import batting_stats_bref


# class for season
class Season:                                               # TODO add in ['League': Team.league] column to data frame
    def __init__(self):
        self.games = 1
        self.data_df = pd.DataFrame(columns={'Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team'})

    def nextGame(self):
        self.data_df = self.data_df[['Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team']]
        self.data_df = self.data_df.append({'Game': self.games, 'Home Team Score': game.score[0],
                                            'Away Team Score': game.score[1], 'Home Team': teams.home,
                                            'Away Team': teams.away}, ignore_index=True)
        pd.set_option("display.max_rows", 162)
        self.games = self.games + 1


# class for game (parent class of inning)
class Game:
    def __init__(self):
        self.inning = 1
        self.outs = 0
        self.score = [0, 0]
        self.top = False

    def runScored(self):
        if self.top:                        # if top of the inning points awarded to the team of index zero
            self.score[1] = self.score[1] + 1
        else:                               # points awarded to team of index one in the bottom of innings
            self.score[0] = self.score[0] + 1

    def out(self):
        self.outs = self.outs + 1
        if self.outs == 3:                  # at three outs switch the inning, resetting outs to zero
            self.outs = 0
            inning.inningSwitch()
            if not game.top:                # if its the bottom of the inning, start next inning
                self.inning = self.inning + 1

        if self.inning >= 10 and self.score[0] != self.score[1]:        # if 10 innings reached and not tied
            season.nextGame()                                           # game ends, go to next game
            self.endGame()
        elif self.inning == 10 and self.score[0] == self.score[1]:      # otherwise, keep going until one team wins
            pass

    def endGame(self):
        self.inning = 1
        self.outs = 0
        self.score = [0, 0]
        self.top = False


# class for innings (child class of game)
class Inning(Game):
    def inningSwitch(self):                 # sets outs back to zero and switches between top and bottom of inning
        if game.top:
            self.outs = 0
            self.bottomOf()
        else:
            self.outs = 0
            self.topOf()

    def topOf(self):                        # if top of inning, set top to true
        game.top = True

    def bottomOf(self):                     # if bottom of inning, sets top to false
        game.top = False


class Batter:
    def __init__(self):
        self.strikes = 0
        self.balls = 0

    def strike(self):
        self.strikes = self.strikes + 1
        if self.strikes == 3:               # if batter has 3 strikes, batter out
            game.out()
            self.nextBatter()               # calls function to get stats on the next batter

    def ball(self):
        self.balls = self.balls + 1
        if self.balls == 4:                 # if batter gets 4 balls
            self.single()                   # walk to first
            self.nextBatter()               # calls function to get the next batters stats

    def nextBatter(self):
        self.strikes = 0
        self.balls = 0
        pass                                # get next batters statistics

    def single(self):
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

    def double(self):
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

    def triple(self):
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

    def homeRun(self):
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


class Bases:
    def __init__(self):
        self.first = False
        self.second = False
        self.third = False
        self.basesLoaded = False

    def loadedBases(self):                  # if there are players on every base, bases are loaded
        if self.first and self.second and self.third:
            self.basesLoaded = True
        else:                               # otherwise bases are not loaded
            self.basesLoaded = False

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


class Team:
    def __init__(self, teamName):
        self.team = teamName
#         self.league = "MLB-AL"

    def getBattingRoster(self):
        batting = batting_stats_bref(2018)
        batting_df = pd.DataFrame(batting)
        batting_df.set_index("Tm", inplace=True)
        homeBat_df = batting_df.loc[self.team]
        return homeBat_df

    def getPitchingRoster(self):
        pitching = pitching_stats_bref(2018)
        pitching_df = pd.DataFrame(pitching)
        pitching_df.set_index("Tm", inplace=True)
        homePitch_df = pitching_df.loc[self.team]
        return homePitch_df

    def getLeague(self):
        pitching = pitching_stats_bref(2018)
        pitching_df = pd.DataFrame(pitching)
        pitching_df.set_index("Tm", inplace=True)
        homePitching_df = pitching_df.loc[self.team]
        league_df = homePitching_df.loc[:, "Lev"]
        self.league = league_df.iloc[0]                 # TODO fix this warning


# class for team (parent class to Home and Away)
class teamsPlaying:
    def __init__(self):
        self.home = '\0'
        self.away = '\0'

    def teams(self, home, away):
        self.home = home
        self.away = away


# class for home games (child class of Team)
class Home(teamsPlaying):
    def getStadiumAdjust(self):
        pass


# class for away games (child class of Team)
class Away(teamsPlaying):
    def getStadiumAdjust(self):
        pass


# class for player (Parent class to Pitcher, Reliever, Positional, and DesignatedHitter)
class Player:
    def __init__(self, playerID):                   # Need to find a way of identifying what position a player plays
        self.playerID = playerID

    def inningsPitched(self):
        pitching = pitching_stats_bref(2018)
        pitching_df = pd.DataFrame(pitching)
        pitching_df.set_index("Name", inplace=True)
        pitch_df = pitching_df.loc[self.playerID]
        IP = pitch_df.loc['IP']
        return IP

    def position(self):
        global player_df
        IP = self.inningsPitched()
        if 10 < IP < 60:
            player_df = Reliever.getRelieverStats(self.playerID)
        elif IP > 60:
            player_df = Pitcher.getPitcherStats(self.playerID)
        else:
            Positional(self.playerID)
        return player_df


# class for pitchers (child class of Player)
class Pitcher(Player):
    def getPitcherStats(self):
        pitcher = pitching_stats_bref(2018)
        pitcher_df = pd.DataFrame(pitcher)
        pitcher_df.set_index("Name", inplace=True)
        player_df = pitcher_df.loc[self.playerID]
        return player_df

    def getStat(self, stat):
        pitcher_stat = player_df.loc[stat]
        return pitcher_stat


# class for relievers (child class of Player)
class Reliever(Player):
    def getRelieverStats(self):
        reliever = pitching_stats_bref(2018)
        reliever_df = pd.DataFrame(reliever)
        reliever_df.set_index("Name", inplace=True)
        player_df = reliever_df.loc[self.playerID]
        return player_df

    def getStat(self, stat):
        player_stat = player_df.loc[stat]
        return player_stat


# class for positional player (child class of Player)
class Positional(Player):
    pass


# class for designated hitters (child class of Player)
class DesignatedHitter(Player):
    def getBatterStats(self):
        batter = batting_stats_bref(2018)
        batter_df = pd.DataFrame(batter)
        batter_df.set_index("Name", inplace=True)
        player_df = batter_df.loc[self.playerID]
        return player_df

    def getStat(self, stat):
        player_stat = player_df.loc[stat]
        return player_stat


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
        elif bases.basesLoaded:                                         # Bases Loaded
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
        elif bases.basesLoaded:                                         # Bases Loaded
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
        elif bases.basesLoaded:                                         # Bases Loaded
            RE = 0.736                                                  # Run Expectancy
    return RE


# initializing objects
season = Season()
game = Game()
inning = Inning()
batter = Batter()
bases = Bases()
teams = teamsPlaying()
home = Home()
away = Away()

# Create objects for each team in the MLB
Braves = Team("Atlanta")
RedSox = Team("Boston")
Phillies = Team("Philadelphia")
Cardinals = Team("St. Louis")
Astros = Team("Houston")
Giants = Team("San Francisco")
BlueJays = Team("Toronto")
Brewers = Team("Milwaukee")
Reds = Team("Cincinnati")
Padres = Team("San Diego")
Mariners = Team("Seattle")
Indians = Team("Cleveland")
Marlins = Team("Miami")
Orioles = Team("Baltimore")
Tigers = Team("Detroit")
Twins = Team("Minnesota")
Rangers = Team("Texas")
Pirates = Team("Pittsburgh")
Athletics = Team("Oakland")
Nationals = Team("Washington")
Rays = Team("Tampa Bay")
Diamondbacks = Team("Arizona")
Royals = Team("Kansas City")
Rockies = Team("Colorado")


# TODO find what to do with cities that have more than 1 team
WhiteSox = Team("Chicago")
Cubs = Team("Chicago")
Yankees = Team("New York")
Mets = Team("New York")
Dodgers = Team("Los Angeles")
Angels = Team("Los Angeles")


# run the game
while season.games < 163:
    swing = uniform(0.0, 1.0)
    if swing <= 0.635:                              # batters swing at 63.5% of all pitches
        strikeZone = uniform(0.0, 1.0)
        if strikeZone <= 0.45:                      # 45% of all pitches are inside the strike zone
            hit = uniform(0.0, 1.0)
            if hit <= 0.8075:                       # 80.75% of swings in strike zone will hit
                expectancy = getRunExpectancy()
                runChance = uniform(0.0, 3.0)
                if runChance <= expectancy:
                    game.runScored()
                else:
                    game.out()
            else:                                   # swing and miss, resulting in a strike
                batter.strike()
        else:                                       # not in strike zone but still swing, results in strike
            batter.strike()
    else:                                           # batter did not swing and not in strike zone, results in a ball
        batter.ball()
    if bases.first:
        throwOut = uniform(0.0, 1.0)
        if throwOut <= 0.3:
            game.out()
            bases.first = False
        else:
            pass
    elif bases.second:
        throwOut = uniform(0.0, 1.0)
        if throwOut <= 0.3:
            game.out()
            bases.second = False
        else:
            pass
    elif bases.third:
        throwOut = uniform(0.0, 1.0)
        if throwOut <= 0.3:
            game.out()
            bases.third = False
        else:
            pass


print("________________________________________\n")
print(season.data_df)
print("________________________________________\n")
