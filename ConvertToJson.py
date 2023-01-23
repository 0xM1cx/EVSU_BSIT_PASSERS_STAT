import string
import csv
import json

letters = string.ascii_uppercase


'''

AUTHOR: Shawn Michael A. Sudaria
GITHUB: https://github.com/0xM1cx
STATUS: In Development

DESCRIPTION: 
The goal of this file is to parse the data in the csv files
and put them all into a json file to be accessed by the 
getStatistics.py file for it to be displayed graphically

'''

def importToJSON(data):
    with open("DATA.json", "w") as jsonFILE:
        json.dump(data, jsonFILE, indent=8)

def getPassers():

    courses_dict = {
            'BEED': [], 
            'BS Ind. Tech. GAP': [], 
            'BS Ind. Tech. E': [],
            'BSF': [], 
            'BSMATH': [], 
            'BTVTED HVART': [], 
            'BSOA': [], 
            'BTVED AFA': [], 
            'BSIT': [], 
            'BSE': [], 
            'BS Ind. Tech. ELX': [], 
            'BAEL': [], 
            'BSID': [], 
            'BSCE': [], 
            'BSED SCI': [], 
            'BS Ind. Tech. CA': [], 
            'BPED': [], 
            'BSHM': [], 
            'BENS': [], 
            'BSIENG': [], 
            'BSND': [], 
            'BTVTED FSM': [], 
            'BSFi': [], 
            'BSARCH': [], 
            'BSMT AT': [], 
            'BSA': [], 
            'BSED MATH': [], 
            'BSEE': [], 
            'BSM': [], 
            'BSECON': [], 
            'BSME': [], 
            'BSCHE': [], 
            'BSECE': [], 
            'BTVTED GFD': [], 
            'BSAGRI': [], 
            'BSCHEM': [], 
            'BCAEd': [], 
            'BSSTAT': [], 
            'BTLED HE': [], 
            'BSE ENGLISH': [], 
            'BTLED IA': [], 
            'BSGE': [], 
            'BSMT MS': [], 
            'BS Ind. Tech. CC': [],
            'BTVED AT': [],
            'BTVED CCT': [],
            'BS Ind. Tech. RAC': [],
            'BTVED ET': [],
            'BS Ind. Tech. CFD': [],
            'BSMT WF': []
        }

    # loop through every csv file that are sorted alphabetically
    for i in letters:
        try:
            with open(f"CSV/EVSU-College-Admission-Application-Result-SY-2021-2022-{i}.csv") as file:
                reader = csv.reader(file)
                
                for row in reader: # This loops through the rows inside every CSV files
                    if row[5] != "PROGRAM":
                        courses_dict[row[5]].append(f"{row[2]}, {row[3]} {row[4]}")
           
        except FileNotFoundError:   
            print("File Not Found, Skipping...")

    JSON_DATA  = json.dumps(courses_dict, indent=8)

    loaded = json.loads(JSON_DATA)

    return loaded            



json_DATA = getPassers()
importToJSON(json_DATA)