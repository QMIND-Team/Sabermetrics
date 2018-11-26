import csv
import pybaseball as bball

def team_pitching_csv():
    out_file = open('team_pitching_headers.csv', 'w', newline = '')
    writer = csv.writer(out_file)
    df = bball.team_pitching(2000)
    headers = list(df.columns)
    writer.writerow(headers)
    out_file.close()

def fan_graphs_csv():
    # get a list of the headers for the function
    pitching_statistics = pitching_stats(2016, 2017)
    pitch_stats_df = pd.DataFrame(pitching_statistics)
    headers = np.asarray(pitch_stats_df.columns)

    with open("fanGraphs.csv", 'w') as csvFile:
        wr = csv.writer(csvFile, dialect='excel')
        wr.writerow(headers)
    csvFile.close()


team_pitching_csv()
fan_graphs_csv()
