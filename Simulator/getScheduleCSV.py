from bs4 import BeautifulSoup as Soup
import requests
import pandas as pd
import numpy as np


url = 'https://www.baseball-reference.com/leagues/MLB/2014-schedule.shtml'
page = requests.get(url)
soup = Soup(page.text, 'html.parser')
tags = soup.find_all("p", attrs={'class': 'game'})
data = []
for tag in tags:
    contents = [text.strip() for text in tag.get_text().split('\n')]
    homeTeam = contents[1]
    awayTeam = contents[4]
    try:
        homeTeamScore = int(contents[2].lstrip('(').rstrip(')'))
        awayTeamScore = int(contents[5].lstrip('(').rstrip(')'))
    except ValueError:
        homeTeamScore = np.nan
        awayTeamScore = np.nan
    if (not any(char.isnumeric() for char in homeTeam)) and (not any(char.isnumeric() for char in awayTeam)):
        data += [[homeTeam, awayTeam, homeTeamScore, awayTeamScore]]

schedule = pd.DataFrame(data=data, columns=["Home Team", "Away Team", "Home Team Score", "Away Team Score"])
schedule.to_csv(r'2014_schedule.csv')


team_dict = {""}
data = [[team, 1500] for team in list(schedule['Home Team'].unique())]
df = pd.DataFrame(data=data, columns=['Team', 'Elo Rating'])
df.to_csv('elo_ratings.csv')
