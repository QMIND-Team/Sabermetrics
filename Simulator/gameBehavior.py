from Simulator import Simulation as sim
import pandas as pd
import warnings

warnings.simplefilter("ignore")

# indicate to simulator that game is being hardcoded
sim.season.hardCoding = True

# Data Frame headings for a hardcoded game
game_df = pd.DataFrame(columns={"Inning", "Home score", "Away score", "Strikes", "Balls", "Outs"})

'''
Possible hardcoding function to simulate the behavior of a baseball game:
    sim.game.runScored()    -> awards a point to which ever team is at bat during this part of the inning
    sim.game.out()          -> increases the number of outs in an inning, three will result in a inningSwitch
    sim.batter.strike()     -> increases the number of strikes a batter has, three will result in an out
    sim.batter.ball()       -> increases the number of balls a batter has, four will result in a single
    sim.batter.single()     -> player gets to first and any base runners present will advance by one base
    sim.batter.double()     -> player gets to second and all base runners present will advance by two bases 
    sim.batter.triple()     -> player gets to third and all base runners present will advance by three bases
    sim.batter.homeRun()    -> player will score a run and all base runners present will also score runs
    sim.bases.playerOn()    -> displays the status of each base, whether there is a player on the bases

    inputData(dataFrame) will append the data the status of game to the game_df
'''


# method to update the data frame of events occurring in the hard coded game
def inputData(dataFrame):
    dataFrame = dataFrame[["Inning", "Home score", "Away score", "Strikes", "Balls", "Outs"]]
    dataFrame = dataFrame.append(
        {"Inning": sim.game.inning, "Home score": sim.game.score[0], "Away score": sim.game.score[1],
         "Strikes": sim.batter.strikes, "Balls": sim.batter.balls, "Outs": sim.game.outs},
        ignore_index=True)
    return dataFrame


#
def battingRecord():
    strikes = sim.batter.strikes
    balls = sim.batter.balls
    print("Batting record : {} strikes, and {} balls".format(strikes, balls))


# top of inning 1
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 1
game_df = inputData(game_df)


# bottom of inning 1
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 1
game_df = inputData(game_df)


# top of inning 2
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.double()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 2
game_df = inputData(game_df)


# bottom of inning 2
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 2
game_df = inputData(game_df)


# top of inning 3
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 3
game_df = inputData(game_df)


# bottom of inning 3
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 3
game_df = inputData(game_df)


# top of inning 4
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 4
game_df = inputData(game_df)


# bottom of inning 4
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 4
game_df = inputData(game_df)


# top of inning 5
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 5
game_df = inputData(game_df)


# bottom of inning 5
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 5
game_df = inputData(game_df)


# top of inning 6
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 6
game_df = inputData(game_df)


# bottom of inning 6
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 6
game_df = inputData(game_df)


# top of inning 7
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 7
game_df = inputData(game_df)


# bottom of inning 7
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 7
game_df = inputData(game_df)


# top of inning 8
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 8
game_df = inputData(game_df)


# bottom of inning 8
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of bottom of inning 8
game_df = inputData(game_df)


# top of inning 9
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()     # End of top of inning 9
game_df = inputData(game_df)


# bottom of inning 9
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)
sim.batter.strike()
game_df = inputData(game_df)

sim.game.out()          # End of bottom of inning 9, End of game 1


print("_________________________________________________________________________________\n")
game_df = game_df.set_index("Inning")
print(game_df)
print("_________________________________________________________________________________\n")
