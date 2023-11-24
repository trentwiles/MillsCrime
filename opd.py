import requests
import csv
from io import StringIO

def getOpenData():
    dat = requests.get("https://data.oaklandca.gov/api/views/wau4-95ys/rows.csv?fourfour=wau4-95ys&accessType=DOWNLOAD")
    csv_data = StringIO(dat.text)

    reader = csv.reader(csv_data)
    for row in reader:
        # Format: TYPE, TIMESTAMP, CASEID, DESCRIPTION, POLICEBEAT
        print(row)

print(getOpenData())