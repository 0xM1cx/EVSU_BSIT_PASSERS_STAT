import matplotlib
import string
import csv
import json

letters = string.ascii_uppercase
# with open("NumberOfBSITPassers.txt", "r") as f:
#     NumberOfPassers = []
#     lines = f.readlines()
#     for i in lines:
#         if i == " ":
#             print("blackline")
#         else:
#             print(i)
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
            'BS Ind. Tech. CC': []
        }
    
    name = []
    for i in letters:
        try:
            with open(f"CSV/EVSU-College-Admission-Application-Result-SY-2021-2022-A.csv") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[5] != "PROGRAM":
                        name.append(row[2])
                        name.append(row[3])
                        name.append(row[4])
                        courses_dict[row[5]].append(f"{row[2]}, {row[3]} {row[4]}")
            JSON_DATA  = json.dumps(courses_dict, indent=8)
            # print(JSON_DATA)
        except FileNotFoundError:
            print("File Not Found, Skipping...")

getPassers()