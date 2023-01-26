import matplotlib.pyplot as akonplotter
import json
import math
'''
AUTHOR: Shawn Michael A. Sudaria
GITHUB: https://github.com/0xM1cx
STATUS: Polishing

DESCRIPTION:
The goal of this file is to parse the DATA.json file
and display them in a bar graph.

'''

# ===== TODO =====
# + Compare the results of this program to the pdf file
# check if the number of passers are the same
# + Change the font size of the x axis labels to fit

# Get the json data from the DATA.json file adn returns them
def getJsonData():
    with open("DATA.json", "r") as data:
        json_data = json.load(data) 
    return json_data

# Get the number of students per key in the json_data dict
def getStats(data):
    # Program Generated List of courses found in the pdf files
    courses_dict = {
        'BEED': 0, 
        'BS Ind. Tech. GAP': 0,  
        'BS Ind. Tech. E': 0, 
        'BSF': 0,  
        'BSMATH': 0, 
        'BTVTED HVART': 0, 
        'BSOA': 0, 
        'BTVED AFA': 0,  
        'BSIT': 0,  
        'BSE': 0,  
        'BS Ind. Tech. ELX': 0,  
        'BAEL': 0,  
        'BSID': 0,  
        'BSCE': 0,  
        'BSED SCI': 0, 
        'BS Ind. Tech. CA': 0,  
        'BPED': 0,  
        'BSHM': 0, 
        'BENS': 0,  
        'BSIENG': 0,  
        'BSND': 0,  
        'BTVTED FSM': 0,  
        'BSFi': 0, 
        'BSARCH': 0,  
        'BSMT AT': 0, 
        'BSA': 0, 
        'BSED MATH': 0, 
        'BSEE': 0, 
        'BSM': 0,  
        'BSECON': 0, 
        'BSME': 0, 
        'BSCHE': 0, 
        'BSECE': 0,  
        'BTVTED GFD': 0, 
        'BSAGRI': 0, 
        'BSCHEM': 0, 
        'BCAEd': 0, 
        'BSSTAT': 0, 
        'BTLED HE': 0, 
        'BSE ENGLISH': 0, 
        'BTLED IA': 0, 
        'BSGE': 0, 
        'BSMT MS': 0, 
        'BS Ind. Tech. CC': 0,
        'BTVED AT': 0,
        'BTVED CCT': 0,
        'BS Ind. Tech. RAC': 0,
        'BTVED ET': 0,
        'BS Ind. Tech. CFD': 0,
        'BSMT WF': 0
    }


    # This loop gets the keys and appends the lengths of their
    # value and storin them in the course_dict dictionary.
    for key in courses_dict.keys():
        courses_dict[key] = int(len(data[key]))

    print(courses_dict.items())
    return courses_dict

# Display the statistical data of the passers
def displayStatData(course_dict):
    degree_Programs = list(course_dict.keys()) # Getting the degree programs from the dictionary and making them into a list 
    numOfPassers = list((course_dict.values())) # Getting the values of the dict, which are the lengths the the array value or the rnumber of students
    
    print(numOfPassers)
    # Draws the figure given the dimensions
    fig =  akonplotter.figure(figsize=(600, 40))
    
    akonplotter.barh(degree_Programs, numOfPassers, color="blue")
    
    akonplotter.title("EVSU Class of 2021-2022 Passers")
    akonplotter.xlabel("Number of Passers", fontsize=5)
    akonplotter.ylabel("Degree Programs")
    akonplotter.xticks(rotation=90)
    
    akonplotter.show()

data = getJsonData() # This is used to get the json data from the DATA.json file
course_dict = getStats(data) # This is used to determine 
displayStatData(course_dict)