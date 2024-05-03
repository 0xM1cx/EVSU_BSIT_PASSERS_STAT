import matplotlib.pyplot as akonplotter
import json
import math
import numpy as np
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

# Get the number of students per key in the json_data dict | temp
def getStats():
    # Program Generated List of courses found in the pdf files
    courses_dict = {
        'BEED': 200, 
        'BIndTech AT': 50,  
        'BIndTech CUL': 50, 
        'BSF': 50,  
        'BSMATH': 80, 
        'BSOA': 135, 
        'BSIT': 180,  
        'BSES': 80,  
        'BIndTech ELX': 50,  
        'BAEL': 100,  
        'BSID': 60,  
        'BSCE': 160,  
        'BSED SCI': 150, 
        'BIndTech PMT': 50,  
        'BPED': 150,  
        'BSHM': 180, 
        'BSND': 100,  
        'BSARCH': 90,  
        'BSA': 225, 
        'BSED MATH': 150, 
        'BSECON': 50, 
        'BSCHE': 40, 
        'BSCHEM': 35, 
        'BCAEd': 100, 
        'BSSTAT': 50, 
        'BIndTech MT': 50,
        'BIndTech ET': 50,
        'BIndTech HVACRT': 50,
        'BIndtTech WFT': 50,
        'BSE': 135,
        'BSBA MM': 90,
        'BIndTech AFT': 50,
        'BTLED HE': 150,
        'BTLED IA': 150,
        'BTVTED FSM': 100,
        'BTVTED GFD': 100,
        'BSME': 120,
        'BSECE': 80,
        'BSGE': 40,
        'BSIENG': 80,
        'BSEE': 120
    }


    # This loop gets the keys and appends the lengths of their
    # value and stores them in the course_dict dictionary.
    # for key in courses_dict.keys():
    #     courses_dict[key] = int(len(data[key]))

    # print(courses_dict.items())
    return courses_dict

# Display the statistical data of the passers
def displayStatData(course_dict):
    degree_Programs = list(course_dict.keys()) # Getting the degree programs from the dictionary and making them into a list 
    numOfPassers = list((course_dict.values())) # Getting the values of the dict, which are the lengths the the array value or the rnumber of students
    
    print(numOfPassers)
    # Draws the figure given the dimensions
    fig =  akonplotter.figure(figsize=(600, 40))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
              '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
              '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5']
    bars = akonplotter.barh(degree_Programs, numOfPassers, color=colors)

    akonplotter.title("EVSU 2024-2025 Passers")
    akonplotter.xlabel("Number of Passers", fontsize=10)
    akonplotter.ylabel("Degree Programs")
    akonplotter.xticks(rotation=90)
    
    akonplotter.gca().xaxis.set_major_locator(akonplotter.MultipleLocator(10))
    akonplotter.grid(axis='x', linestyle='--', alpha=0.7, color='black')
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    akonplotter.show()

# data = getJsonData() # This is used to get the json data from the DATA.json file
course_dict = getStats() # This is used to determine 
displayStatData(course_dict)