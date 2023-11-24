import requests
import csv
from io import StringIO

def addressToCordinates():
    return 

def getOpenData(timeRange):
    dat = requests.get("https://data.oaklandca.gov/api/views/ym6k-rx7a/rows.csv?fourfour=ym6k-rx7a&accessType=DOWNLOAD")
    csv_data = StringIO(dat.text)

    reader = csv.reader(csv_data)
    for row in reader:
        # Format: TYPE, TIMESTAMP, CASEID, DESCRIPTION, POLICEBEAT
        print(row)
        cordinates = row[8][len("POINT ("):][:-1].split(" ")
        print(cordinates)

print(getOpenData())