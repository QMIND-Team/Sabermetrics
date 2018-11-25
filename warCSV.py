
import csv
from pybaseball import bwar_pitch

def bwar_csv():
    out_file = open('bwar.csv', 'w', newline = '')
    writer = csv.writer(out_file)
    df = bwar_pitch()
    headers = list(df.columns)
    writer.writerow(headers)
    out_file.close()
bwar_csv()