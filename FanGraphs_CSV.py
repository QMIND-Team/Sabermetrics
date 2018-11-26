import pandas as pd
import numpy as np
import csv

from pybaseball import pitching_stats

# get a list of the headers for the function
pitching_statistics = pitching_stats(2016, 2017)
pitch_stats_df = pd.DataFrame(pitching_statistics)
headers = np.asarray(pitch_stats_df.columns)

with open("fanGraphs.csv", 'w') as csvFile:
    wr = csv.writer(csvFile, dialect='excel')
    wr.writerow(headers)
csvFile.close()
