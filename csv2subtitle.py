# This script converts csv files to srt files with speaker names.

import glob
import csv
import os

def sec2timestamp(sec):
    # Convert seconds to timestamp
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}:{:02d},{:03d}".format(int(h), int(m), int(s), int(sec*100%100))


def make_srt(csvfile, outfile):
    with open(csvfile, 'r') as f, open(outfile, 'w') as f_out:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            start, end, speaker, text = row

            start, end = float(start), float(end)
            f_out.write(f'{i+1}\n')
            f_out.write(f'{sec2timestamp(float(start))} --> {sec2timestamp(float(end))}\n')
            f_out.write(f'{speaker} : {text}\n\n')


if __name__ == '__main__':
    csvfiles = glob.glob('csv/**/*.csv')
    for csvfile in csvfiles:
        outfile = csvfile.replace('csv', 'srt')
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        make_srt(csvfile, outfile)