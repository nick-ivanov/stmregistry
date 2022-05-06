# Draft. Not final yet.

import csv
with open('raw_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print('||'.join(row))
        print("----")
    