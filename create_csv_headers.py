import csv
import pybaseball as bball

def team_pitching_csv():
    out_file = open('team_pitching_headers.csv', 'w', newline = '')
    writer = csv.writer(out_file)
    df = bball.team_pitching(2000)
    headers = list(df.columns)
    writer.writerow(headers)
    out_file.close()
team_pitching_csv()


def bwar_csv():
    out_file = open('bwar.csv', 'w', newline = '')
    writer = csv.writer(out_file)
    df = bwar_pitch()
    headers = list(df.columns)
    writer.writerow(headers)
    out_file.close()
bwar_csv()