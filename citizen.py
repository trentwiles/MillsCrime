import requests
import time

LOWER_LAT = str(37.770779600332716)
UPPER_LAT = str(37.79013434508991)
LOWER_LON = str(-122.20010941364336)
UPPER_LON = str(-122.1595657163046)

FA_ICONS = {"stabbing": '<i class="fa-solid fa-gun fa-fade"></i>', 
            "sideshow": '<i class="fa-solid fa-car fa-fade"></i>',
            "robbery": '<i class="fa-solid fa-sack-dollar fa-fade"></i>',
            "armed_robbery": '<i class="fa-solid fa-people-robbery fa-fade"></i>',
            "fire": '<i class="fa-solid fa-fire fa-fade"></i>',
            "police": '<i class="fa-solid fa-shield-halved fa-fade"></i>',
            "other": '<i class="fa-solid fa-circle-exclamation fa-fade"></i>'}

def getRanges():
    return {"upperLon": float(UPPER_LON), "upperLat": float(UPPER_LAT), "lowerLat": float(LOWER_LAT), "lowerLon": float(LOWER_LON)}

def determineIcon(text):
    text = text.lower()
    if "gunshot" in text or "stabbing" in text or "assault" in text or "firearm":
        return FA_ICONS["stabbing"]
    if "fire" in text or "smoke" in text:
        return FA_ICONS["fire"]
    if "sideshow" in text or "collides" in text or "crash" in text or "vehicle" in text:
        return FA_ICONS["sideshow"]
    if "armed" in text or "robbery" in text:
        return FA_ICONS["armed_robbery"]
    if "police" in text:
        return FA_ICONS["police"]
    if "stolen" in text or "robbery" in text:
        return FA_ICONS["robbery"]
    return FA_ICONS["other"]

def getReports(timeRange):
    dataHolder = []
    # timeRange is in hours
    timeRange = timeRange * 3600
    #print(timeRange)
    r = requests.get(f"https://citizen.com/api/incident/trending?lowerLatitude={LOWER_LAT}&lowerLongitude={LOWER_LON}&upperLatitude={UPPER_LAT}&upperLongitude={UPPER_LON}&fullResponse=true&limit=2000")
    for incident in r.json()['results']:
        age = round(time.time() - incident["cs"]/1000)
        if timeRange >= age:
            dataToSend = {"timestamp": incident["cs"]/1000, "cordinates": [incident["latitude"], incident["longitude"]], "details": incident["raw"], "address": incident["location"], "icon": determineIcon(incident["raw"])}
            dataHolder.append(dataToSend)
    
    return dataHolder