import Simulator
import warnings
import numpy as np
from Simulator import Team

# declaring __all__ to allow for proper importing
Simulator.__all__ = ['NL', 'AL']

# ignore warnings in code
warnings.simplefilter("ignore")


# Create objects for each Team in the MLB-NL
Cubs = Team.Team("Cubs", "Chicago", "MLB-NL")
Dodgers = Team.Team("Dodgers", "Los Angeles", "MLB-NL")
Cardinals = Team.Team("Cardinals", "St. Louis", "MLB-NL")
Mets = Team.Team("Mets", "New York", "MLB-NL")
Pirates = Team.Team("Pirates", "Pittsburgh", "MLB-NL")
Nationals = Team.Team("Nationals", "Washington", "MLB-NL")
Braves = Team.Team("Braves", "Atlanta", "MLB-NL")
Brewers = Team.Team("Brewers", "Milwaukee", "MLB-NL")
Reds = Team.Team("Reds", "Cincinnati", "MLB-NL")
Phillies = Team.Team("Philies", "Philadelphia", "MLB-NL")
Giants = Team.Team("Giants", "San Francisco", "MLB-NL")
Rockies = Team.Team("Rockies", "Colorado", "MLB-NL")
Diamondbacks = Team.Team("Diamondbacks", "Arizona", "MLB-NL")
Padres = Team.Team("Padres", "San Diego", "MLB-NL")
Marlins = Team.Team("Marlins", "Miami", "MLB-NL")

# Create objects for each Team in the MLB-AL
Yankees = Team.Team("Yankees", "New York", "MLB-AL")
RedSox = Team.Team("RedSox", "Boston", "MLB-AL")
Indians = Team.Team("Indians", "Cleveland", "MLB-AL")
Astros = Team.Team("Astros", "Houston", "MLB-AL")
WhiteSox = Team.Team("WhiteSox", "Chicago", "MLB-AL")
Athletics = Team.Team("Athletics", "Oakland", "MLB-AL")
Orioles = Team.Team("Orioles", "Baltimore", "MLB-AL")
Rays = Team.Team("Rays", "Tampa Bay", "MLB-AL")
Angels = Team.Team("Angels", "Los Angeles", "MLB-AL")
BlueJays = Team.Team("BlueJays", "Toronto", "MLB-AL")
Twins = Team.Team("Twins", "Minnesota", "MLB-AL")
Royals = Team.Team("Royals", "Kansas City", "MLB-AL")
Mariners = Team.Team("Mariners", "Seattle", "MLB-AL")
Rangers = Team.Team("Rangers", "Texas", "MLB-AL")
Tigers = Team.Team("Tigers", "Detroit", "MLB-AL")

# creating an array of Team objects for all teams in NL
NL = np.array([Cubs, Dodgers, Cardinals, Mets, Pirates, Nationals, Braves, Brewers, Reds,
               Phillies, Giants, Rockies, Diamondbacks, Padres, Marlins])
# creating an array of Team objects for all teams in AL
AL = np.array([Yankees, RedSox, Indians, Astros, WhiteSox, Athletics, Orioles, Rays, Angels,
               BlueJays, Twins, Royals, Mariners, Rangers, Tigers])
