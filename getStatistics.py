import matplotlib.pyplot as akonplotter
import json

# ===== TODO =====
# + Compare the results of this program to the pdf file
# check if the number of passers are the same
# + Change the font size of the x axis labels to fit

# Get the json data from the DATA.json file
def getJsonData():
    with open("DATA.json", "r") as data:
        json_data = json.load(data) 

    return json_data

# Get the number of students per key in the json_data dict
def getStats(data):
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

    for key in courses_dict.keys():
        courses_dict[key] = len(data[key])

    print(courses_dict.items())
    return courses_dict


# Display the statistical data of the passers
def displayStatData(course_dict):
    degree_Programs = list(course_dict.keys()) 
    numOfPassers = list(course_dict.values())
    print(numOfPassers)
    fig =  akonplotter.figure(figsize=(40, 40))

    akonplotter.barh(degree_Programs, numOfPassers, color="blue")

    akonplotter.title("EVSU Class of 2021-2022 Passers")
    akonplotter.xlabel("Number of Passers", fontsize=0.2)
    akonplotter.ylabel("Degree Programs")
    akonplotter.xticks(rotation=90)
    
    akonplotter.show()

data = getJsonData()
course_dict = getStats(data)
displayStatData(course_dict)