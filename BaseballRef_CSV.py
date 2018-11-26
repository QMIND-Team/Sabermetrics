import pandas as pd
import numpy as np
import csv

from pybaseball import pitching_stats_bref

# get a list of the headers for the function
pitching_statistics = pitching_stats_bref(2016)
pitch_stats_df = pd.DataFrame(pitching_statistics)
headers = np.asarray(pitch_stats_df.columns)

with open("baseballRef.csv", 'w') as csvFile:
    wr = csv.writer(csvFile, dialect='excel')
    wr.writerow(headers)
csvFile.close()
