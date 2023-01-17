import matplotlib
import string
import csv

letters = string.ascii_uppercase


# with open("NumberOfBSITPassers.txt", "r") as f:
#     NumberOfPassers = []
#     lines = f.readlines()
#     for i in lines:
#         if i == " ":
#             print("BlankLine")
#         else:
#             print(i)

def getPassers():
    courses = ['BEED', 'BS Ind. Tech. GAP', 'BS Ind. Tech. E', 'BSF', 
    'BSMATH', 'BTVTED HVART', 'BSOA', 'BTVED AFA', 'BSIT', 'BSE', 'BS Ind. Tech. ELX', 
    'BAEL', 'BSID', 'BSCE', 'BSED SCI', 'BS Ind. Tech. CA', 'BPED', 'BSHM', 'BENS', 'BSIENG', 
    'BSND', 'BTVTED FSM', 'BSFi', 'BSARCH', 'BSMT AT', 'BSA', 'BSED MATH', 'BSEE', 
    'BSM', 'BSECON', 'BSME', 'BSCHE', 'BSECE', 'BTVTED GFD', 'BSAGRI', 'BSCHEM', 'BCAEd', 
    'BSSTAT', 'BTLED HE', 'BSE ENGLISH', 'BTLED IA', 'BSGE', 'BSMT MS', 'BS Ind. Tech. CC']

    for i in letters:
        try:
            with open(f"CSV/EVSU-College-Admission-Application-Result-SY-2021-2022-A.csv") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[5] not in courses and row[5] != "PROGRAM":
                        courses.append(row[5])


        except FileNotFoundError:
            print("File Not Found, Skipping...")

    print(courses)

getPassers()
