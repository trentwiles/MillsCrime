import requests
import csv
from io import StringIO
import citizen
from datetime import datetime
import time

def isCordinatesInRange(lat, lon):
    dat = citizen.getRanges()
    print(dat)
    return (lat in range(int(dat["lowerLat"]), int(dat["upperLat"] + 1))) and (lon in range(int(dat["lowerLon"]), int(dat["upperLon"] + 1)))

def policeBeatInRange(beat):
    return (beat == "28X") or (beat == "25X") or (beat == "29X")

def getOpenData(timeRange):
    dataHolder = []
    # range is in hours
    timeRange = timeRange * 3600

    # process data into readable format
    dat = requests.get("https://data.oaklandca.gov/api/views/ym6k-rx7a/rows.csv?fourfour=ym6k-rx7a&accessType=DOWNLOAD")
    csv_data = StringIO(dat.text)
    reader = csv.reader(csv_data) # drop first row, just contains the headers
    for row in reader:
        # Format: TYPE, TIMESTAMP, CASEID, DESCRIPTION, POLICEBEAT
        # If it isn't the header row
        if row[8] != "Location":
            # If the police beat is near the school
            # Source: https://gisapps1.mapoakland.com/policedistricts/
            if policeBeatInRange(row[4]):
                epoch_time = int(datetime.strptime(row[1], "%m/%d/%Y %I:%M:%S %p").timestamp())
                # If the incident is within the time range
                if timeRange >= (round(time.time()) - epoch_time):
                    cordinates = row[8][len("POINT ("):][:-1].split(" ")
                    cordinates[0] = float(cordinates[0])
                    cordinates[1] = float(cordinates[1])
                    dataToSave = {"timestamp": epoch_time, "cordinates": [cordinates[1], cordinates[0]], "details": row[3], "address": row[5], "icon": citizen.determineIcon(row[3])}
                    dataHolder.append(dataToSave)
    return dataHolder