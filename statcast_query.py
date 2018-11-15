import pandas as pd
import pybaseball as bball

def query():
    statcast_data = bball.statcast_single_game(529429)
    data_df = pd.DataFrame(statcast_data)
    #print(data_df)
    #data_df.to_csv('statcast_single_game_data.csv')

    stroman = bball.playerid_lookup('stroman', 'marcus')

    stroman_data_2018 = bball.statcast_pitcher('2018-04-01', '2018-11-01', 573186)
    stroman_df_2018 = pd.DataFrame(stroman_data_2018)
    stroman_data_2017 = bball.statcast_pitcher('2017-04-01', '2017-11-01', 573186)
    stroman_df_2017 = pd.DataFrame(stroman_data_2017)

    print("2018: ", stroman_df_2018.isnull().sum(axis=0).tolist())
    print("2017: ", stroman_df_2017.isnull().sum(axis=0).tolist())

    vel = stroman_df_2018.drop(stroman_df_2018.columns.difference(['release_speed']), 1, inplace=True)
    print(vel)

