import matplotlib
import json

# Get the json data from the DATA.json file
def getJsonData():
    with open("DATA.json", "r") as data:
        json_data = json.load(data) 

    return json_data

# Get the number of students per key in the json_data dict
def getStats(data):
     

# Display the statistical data of the passers
def displayStatData():
    pass   

data = getJsonData()
getStats(data)