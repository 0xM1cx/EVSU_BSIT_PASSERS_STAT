import string
import csv
import string
from tabula import convert_into_by_batch
from tabula import read_pdf
from subprocess import run

# A little caveat, this only works on linux due to it being able to run wget without any 
# other proprietary syntax like powershell, cmd, etc.

'''
AUTHOR: Shawn Michael A. Sudaria
GITHUB: https://github.com/0xM1cx
STATUS: Polishing

DESCRIPTION
This program has the following features:
1. Download the pdf files from the link given.
2. Convert the downloaded pdf files into csv files and put
them in a CSV folder.
3. Parse the data in the file to be written in a text file.

'''
letters = string.ascii_letters

# FUNCTION TO DOWNLOAD ALL THE PDF FILES ON THE EVSU WEBSITE.
def getPdfFiles():
    for chars in letters.upper():
        run(["wget", f"https://www.evsu.edu.ph/wp-content/uploads/2021/07/EVSU-College-Admission-Application-Result-SY-2021-2022-{chars}.pdf"])
    run(["mkdir", "CSV"])
    run(["cp", "*", "/CSV"])


# FUNCTION TO CONVERT PDF TO CSV
def convertPdfToCSV():
    convert_into_by_batch("./", output_format="csv", pages="all")
    
# FUNCTION FOR EXTRACTING SPECIFIC ROWS FROM A CSV FILE.
def extractCsvRows(letters):
    try:
        for i in letters:
            with open(f"CSV/EVSU-College-Admission-Application-Result-SY-2020-2021-{i.upper()}.csv", "r") as file:
                reader = csv.reader(file)
                rows = [row for row in reader]

            num = 0
            with open("NumberOfBSITPassers.txt", "w") as f:
                for i in rows:
                    if "BSIT" in i and "MAIN CAMPUS (Tacloban)" in i:
                        num += 1
                        f.write(f"{num}) {str(i)}\n")
                    else:
                        continue
                f.write("\n")
            
            with open("passers.txt", "w") as file:
                for b in rows:
                    file.write(b)
    except FileNotFoundError:
        print("File Not Found, skipping...")



def main():
    print("Type 1 to download the pdf files")
    print("Type 2 to extract the tables in the pdf files and convert them to CSV")
    print("Type 3 to get the statistics of the passers")
    user_input = int(input())

    try:
        if user_input == 1:
            getPdfFiles()
        elif user_input == 2:
            convertPdfToCSV()
        elif user_input == 3:
            extractCsvRows(letters)
        else: 
            print("Pick between 1 - 3")
    except:
        print("INPUT MUST BE INTEGER")
main()
