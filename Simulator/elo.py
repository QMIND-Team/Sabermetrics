import pandas as pd
import math

def calculateExpectedScores(R1, R2):
    '''
    Calculates expected scores/win expectancy of both players/entities.
    Expected score is the sum of probability of an entity winning
    and half of the probability of the entity drawing.

    :param int rating1: Elo rating of first entity
    :param int rating2: Elo rating of second entity
    :return tuple expectedScores:
    '''

    expectedScores = (0, 0)

    # first calculate Q1 and Q2
    Q1 = 10 ** (R1 / 400)
    Q2 = 10 ** (R2 / 400)

    # calculate E1 and E2 which are the expected scores
    E1 = Q1 / (Q1 + Q2)
    E2 = 1 - E1 # Q2 / (Q1 + Q2)

    expectedScores = (E1, E2)

    return expectedScores


def calculateNewRating(oldRating, expectedResult, trueResult, kFactor):
    '''
    Calculates the new Elo rating of an entity

    :param int oldRating: previous Elo rating of the entity
    :param float expectedResult: win expectancy for the team
    :param float trueResult: 1 for a win and 0 for a loss
    :param float kFactor: weight constant for the season
    :return int newRating: Elo rating of the entity after game is played
    '''

    newRating = oldRating + (kFactor * (trueResult - expectedResult))
    return int(newRating)


def seasonEloRatings(seasonDF, eloRatings):

    #seasonDF = pd.read_csv(path, index_col=0)
    #eloRatings = pd.read_csv('elo_ratings.csv', index_col=0)

    #print(eloRatings.head())

    for index, row in seasonDF.iterrows():
        homeTeam = row['Home Team']
        awayTeam = row['Away Team']
        homeTeamScore = row['Home Team Score']
        awayTeamScore = row['Away Team Score']
        if (homeTeam not in eloRatings['Team'].unique()):
            eloRatings
        homeEloRating = int(eloRatings.loc[eloRatings['Team'] == homeTeam, 'Elo Rating'])  + 24 # add home team advantage
        awayEloRating = int(eloRatings.loc[eloRatings['Team'] == awayTeam, 'Elo Rating'])
        homeExpected, awayExpected = calculateExpectedScores(homeEloRating, awayEloRating)
        if homeTeamScore > awayTeamScore:
            homeResult = 1
            awayResult = 0
        else:
            homeResult = 0
            awayResult = 1
        runDifferential = abs(homeTeamScore - awayTeamScore)
        kFactor = 0.5 * runDifferential
        newHomeRating = calculateNewRating(homeEloRating, homeExpected, homeResult, kFactor)
        newAwayRating = calculateNewRating(awayEloRating, awayExpected, awayResult, kFactor)
        eloRatings.loc[eloRatings['Team'] == homeTeam, 'Elo Rating'] = newHomeRating
        eloRatings.loc[eloRatings['Team'] == awayTeam, 'Elo Rating'] = newAwayRating

    return eloRatings


def scaleRatings(eloRatings):

    minRating = eloRatings['Elo Rating'].min()
    maxRating = eloRatings['Elo Rating'].max()

    upperBound = 1700
    lowerBound = 1300

    for index, row in eloRatings.iterrows():
        value = row['Elo Rating']
        newValue = lowerBound + ((value - minRating) / (maxRating - minRating) * (upperBound - lowerBound))
        eloRatings.loc[eloRatings['Team'] == row['Team'], 'Elo Rating'] = int(newValue)

    return eloRatings


def playSeason(seasonDF, eloRatings):

    eloRatings = seasonEloRatings(seasonDF, eloRatings)
    return scaleRatings(eloRatings)


def playAllSeasons():

    startYear = 2014
    endYear = 2017

    #seasonDF = pd.read_csv(path, index_col=0)
    eloRatings = pd.read_csv('elo_ratings.csv', index_col=0)

    for year in range(startYear, endYear + 1):
        path = f'{year}_schedule.csv'
        seasonDF = pd.read_csv(path, index_col=0)
        eloRatings = playSeason(seasonDF, eloRatings)

    return eloRatings


eloRatings = playAllSeasons()
print(eloRatings)

