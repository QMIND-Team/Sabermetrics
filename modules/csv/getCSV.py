import pandas as pd
from pybaseball import team_batting, team_pitching, batting_stats_bref, pitching_stats_bref, pitching_stats_range, bwar_pitch, pitching_stats

#teamBattingDF = team_batting(2008, 2018, league="all", ind=1)
#teamPitchingDF = team_pitching(2008, 2018, league="all", ind=1)
battingStatsBrefDF = pd.DataFrame()
pitchingStatsBrefDF = pd.DataFrame()
#pitchingStatsRangeDF = pitching_stats_range('2008-01-01', '2018-01-01')
bWarDF = pd.DataFrame(bwar_pitch(return_all=1))
pitchingFangraphsDF = pd.DataFrame()

for year in range(2008, 2019):

    #newDF1 = batting_stats_bref(season=year)
    #newDF2 = pitching_stats_bref(season=year)
    newDF3 = pitching_stats(year)
#    newDF1['Year'] = year
#    newDF2['Year'] = year

#   battingStatsBrefDF = battingStatsBrefDF.append(newDF1)
#   pitchingStatsBrefDF = pitchingStatsBrefDF.append(newDF2)
    pitchingFangraphsDF = pitchingFangraphsDF.append(newDF3)

# create csvs
#pitchingStatsBrefDF.to_csv(r'modules\csv\pitching_stats_bref.csv')
#battingStatsBrefDF.to_csv(r'modules\csv\batting_stats_bref.csv')
#pitchingStatsRangeDF.to_csv(r'modules\csv\pitching_stats_range.csv')
#teamBattingDF.to_csv(r'modules\csv\team_batting.csv')
#teamPitchingDF.to_csv(r'modules\csv\team_pitching.csv')
bWarDF.to_csv('bwar.csv')
pitchingFangraphsDF.to_csv('pitching_fangraphs.csv')



