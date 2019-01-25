from random import randint
import simpy as sp
import pandas as pd
import numpy as np


# class for season
class Season:
    def __init__(self):
        self.games = 1
        self.data_df = pd.DataFrame(columns=['Runs For', 'Runs Against'])

    def nextGame(self):
        self.data_df = self.data_df.append({'Game': self.games, 'Runs For': game.score[0],
                                            'Runs Against': game.score[1]}, ignore_index=True)
        self.data_df.set_index('Game', inplace=True)
        self.games = self.games + 1
        if self.games == 163:               # add to game count as long as its less than 163
            self.endSeason()                # if 162 games played, season is over

    def endSeason(self):
        pass


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

        if self.inning == 10:
            season.nextGame()
            self.endGame()

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


# class for team (parent class to Home and Away)
class Team:
    def __init__(self, startingPitcher):
        self.startingPitcher = startingPitcher
        pass


# class for home games (child class of Team)
class Home(Team):
    def getParkAdjustment(self):
        pass


# class for away games (child class of Team)
class Away(Team):
    def getParkAdjustment(self):
        pass


# class for player (Parent class to Pitcher, Reliever, Positional, and DesignatedHitter)
class Player:
    def __init__(self, playerID):
        self.playerID = playerID
        pass


# class for pitchers (child class of Player)
class Pitcher(Player):
    pass


# class for relievers (child class of Player)
class Reliever(Player):
    pass


# class for positional player (child class of Player)
class Positional(Player):
    pass


# class for designated hitters (child class of Player)
class DesignatedHitter(Player):
    pass


# initializing objects
season = Season()
game = Game()
inning = Inning()
batter = Batter()
bases = Bases()

