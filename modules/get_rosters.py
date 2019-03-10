from bs4 import BeautifulSoup as Soup
import requests
import time
import pandas as pd
import random


def fetchAllRosters():
    '''
    To get a dictionary where keys are team abbreviations and values are lists of all players in the team.
    '''
    teams = ["ATL", "WSN", "PHI", "NYM", "MIA", "MIL", "CHC", "STL", "PIT", "CIN", "LAD", "COL", "ARI", "SFG", "SDP",
             "BOS", "NYY", "TBR", "TOR", "BAL", "CLE", "MIN", "DET", "CHW", "KCR", "HOU", "OAK", "SEA", "LAA", "TEX"]
    rosters = {}
    for teamName in teams:
        url = f"https://www.baseball-reference.com/teams/{teamName}/2018-roster.shtml"
        res = requests.get(url)
        soup = Soup(res.text, 'html.parser')
        listOfTags = soup.select('tbody tr td a')
        players = []
        for tag in listOfTags:
            players.append(tag.text)
        rosters[teamName] = players
        time.sleep(random.random())
    return rosters


def createTeamRosters(teamName):
    '''
    To get a DataFrame of the latest 40 man roster for the given teamName
    '''
    teamDict = {'Atlanta Braves': 'ATL', 'Washington Nationals': 'WSN', 'Philadelphia Phillies': 'PHI', 'New York Mets': 'NYM',
                'Miami Marlins': 'MIA', 'Milwaukee Brewers': 'MIL', 'Chicago Cubs': 'CHC', 'St. Louis Cardinals': 'STL',
                'Pittsburgh Pirates': 'PIT', 'Cincinnati Reds': 'CIN', 'Los Angeles Dodgers': 'LAD', 'Colorado Rockies': 'COL',
                'Arizona Diamondbacks': 'ARI', 'San Francisco Giants': 'SFG', 'San Diego Padres': 'SDP', 'Boston Red Sox': 'BOS',
                'New York Yankees': 'NYY', 'Tampa Bay Rays': 'TBR', 'Baltimore Orioles': 'BAL', 'Cleveland Indians': 'CLE',
                'Minnesota Twins': 'MIN', 'Detroit Tigers': 'DET', 'Chicago White Sox': 'CHW', 'Kansas City Royals': 'KCR',
                'Houston Astros': 'HOU', 'Oakland Athletics': 'OAK', 'Seattle Mariners': 'SEA', 'Los Angeles Angels': 'LAA',
                'Texas Rangers': 'TEX', 'Toronto Blue Jays': 'TOR'}
    teamAbbreviation = teamDict[teamName]
    url = f"https://www.baseball-reference.com/teams/{teamAbbreviation}/2018-roster.shtml"
    res = requests.get(url)
    soup = Soup(res.text, 'html.parser')
    listOfTags = soup.select('tbody tr td a')
    players = []
    for tag in listOfTags:
        players.append(tag.text)
    rosterDF = pd.DataFrame(data=players)
    return rosterDF
    
