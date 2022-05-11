# Draft. Not final yet.

import csv
with open('raw_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0])
        print("----")
        with open(row[0], "w") as stmfile:
            stmfile.write(f"""<!DOCTYPE html>
            <html>
            <head><title>{row[0]}: STM Registry</title></head>
            <body>
            <h1>{row[0]}</h1>

            <p></p>

            </body>
            </html>""")
    