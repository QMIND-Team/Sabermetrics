from random import uniform
import pandas as pd
import numpy as np

from pybaseball import pitching_stats_bref
from pybaseball import batting_stats_bref


# import schedule from MLB_2019_Schedule
import MLB_2019_Schedule

pd.set_option('display.max_columns', 6)


# class for season
class Season:
    def __init__(self):
        self.games = 1
        self.data_df = pd.DataFrame(columns={'Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team',
                                             'League'})

    def nextGame(self):
        self.data_df = self.data_df[['Game', 'Home Team Score', 'Away Team Score', 'Home Team', 'Away Team']]
        self.data_df = self.data_df.append({'Game': self.games, 'Home Team Score': game.score[0],
                                            'Away Team Score': game.score[1], 'Home Team': playingGame.home,
                                            'Away Team': playingGame.away, 'League': playingGame.gameLeague()},
                                           ignore_index=True)
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
    def __init__(self, teamCity, league):
        self.team = teamCity
        self.league = league

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
        league = self.league
        return league


# class for team (parent class to Home and Away)
class TeamsPlaying:
    def __init__(self, homeTeam, awayTeam):
        self.home = homeTeam
        self.away = awayTeam

    def gameLeague(self):
        for team in range(len(NL)):
            if self.home == NL[team]:
                homeLeague = "MLB-NL"
            if self.away == NL[team]:
                awayLeague = "MLB-NL"
        for team in range(len(AL)):
            if self.home == AL[team]:
                homeLeague = "MLB-AL"
            if self.away == AL[team]:
                awayLeague = "MLB-AL"

        if homeLeague == "MLB-NL" and awayLeague == "MLB-NL":
            league = "MLB-NL"
        elif homeLeague == "MLB-AL" and awayLeague == "MLB-AL":
            league = "MLB-AL"
        else:
            league = "Inter-League"
        return league


# class for home games (child class of Team)
class Home(TeamsPlaying):
    def getStadiumAdjust(self):
        pass


# class for away games (child class of Team)
class Away(TeamsPlaying):
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
playingGame = TeamsPlaying("Athletics", "Mariners")
home = Home("Athletics", "Mariners")
away = Away("Athletics", "Mariners")


# create lists for teams in each MLB league
NL = np.array(["Cubs", "Dodgers", "Cardinals", "Mets", "Pirates", "Nationals", "Braves", "Brewers", "Reds",
               "Phillies", "Giants", "Rockies", "Diamondbacks", "Padres", "Marlins"])
AL = np.array(["Yankees", "RedSox", "Indians", "Astros", "WhiteSox", "Athletics", "Orioles", "Rays", "Angels",
               "BlueJays", "Twins", "Royals", "Mariners", "Rangers", "Tigers"])

# Create objects for each team in the MLB-NL
Cubs = Team("Chicago", "MLB-NL")
Dodgers = Team("Los Angeles", "MLB-NL")
Cardinals = Team("St. Louis", "MLB-NL")
Mets = Team("New York", "MLB-NL")
Pirates = Team("Pittsburgh", "MLB-NL")
Nationals = Team("Washington", "MLB-NL")
Braves = Team("Atlanta", "MLB-NL")
Brewers = Team("Milwaukee", "MLB-NL")
Reds = Team("Cincinnati", "MLB-NL")
Phillies = Team("Philadelphia", "MLB-NL")
Giants = Team("San Francisco", "MLB-NL")
Rockies = Team("Colorado", "MLB-NL")
Diamondbacks = Team("Arizona", "MLB-NL")
Padres = Team("San Diego", "MLB-NL")
Marlins = Team("Miami", "MLB-NL")

# Create objects for each team in the MLB-AL
Yankees = Team("New York", "MLB-AL")
RedSox = Team("Boston", "MLB-AL")
Indians = Team("Cleveland", "MLB-AL")
Astros = Team("Houston", "MLB-AL")
WhiteSox = Team("Chicago", "MLB-AL")
Athletics = Team("Oakland", "MLB-AL")
Orioles = Team("Baltimore", "MLB-AL")
Rays = Team("Tampa Bay", "MLB-AL")
Angels = Team("Los Angeles", "MLB-AL")
BlueJays = Team("Toronto", "MLB-AL")
Twins = Team("Minnesota", "MLB-AL")
Royals = Team("Kansas City", "MLB-AL")
Mariners = Team("Seattle", "MLB-AL")
Rangers = Team("Texas", "MLB-AL")
Tigers = Team("Detroit", "MLB-AL")


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


print("______________________________________________________________________\n")
print(season.data_df)
print("______________________________________________________________________\n")


