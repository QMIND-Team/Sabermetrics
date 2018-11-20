import pandas as pd
import numpy as np
import csv

from pybaseball import pitching_stats_range

# get a list of the headers for the function
pitching_statistics = pitching_stats_range('2016-01-01', '2017-01-01')
pitch_stats_df = pd.DataFrame(pitching_statistics)
headers = np.asarray(pitch_stats_df.columns)

with open("baseballSavant.csv", 'w') as csvFile:
    wr = csv.writer(csvFile, dialect='excel')
    wr.writerow(headers)
csvFile.close()
