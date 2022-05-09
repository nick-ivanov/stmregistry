# Draft. Not final yet.

import csv
with open('raw_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0])
        print("----")
        with open(row[0], "w") as stmfile:
            stmfile.write("<!DOCTYPE html>\n<html><body>Blah.</body></html>")
    