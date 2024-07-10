# This script converts csv files to srt files with rttm files.
# For more information about rttm format : check https://github.com/nryant/dscore#rttm

import glob
import csv
import os


def make_rttm(csvfile, outfile):
    with open(csvfile, 'r') as f, open(outfile, 'w') as f_out:
        episode = os.path.basename(csvfile).split('.')[0]
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            start, end, speaker, text = row

            start, end = float(start), float(end)
            f_out.write(f'SPEAKER {episode} 1 {start:.2f} {end-start:.2f} <NA> <NA> {speaker} <NA> <NA>\n')


if __name__ == '__main__':
    csvfiles = glob.glob('csv/**/*.csv')
    for csvfile in csvfiles:
        outfile = csvfile.replace('csv', 'rttm')
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        make_rttm(csvfile, outfile)