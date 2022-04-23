
import string
import csv
import string
from tabula import convert_into_by_batch
from tabula import read_pdf
from subprocess import run

# A little caveat, this only works on linux due to it being able to run wget without any 
# other proprietary syntax like powershell, cmd, etc.


letters = string.ascii_letters
# FUNCTION TO DOWNLOAD ALL THE PDF FILES ON THE EVSU WEBSITE.
def getPdfFiles():
    for chars in letters.upper():
        run(["wget", f"https://www.evsu.edu.ph/wp-content/uploads/2021/07/EVSU-College-Admission-Application-Result-SY-2021-2022-{chars}.pdf"])
    run(["mkdir", "CSV"])
    run(["cp", "*", "/CSV"])


#FUNCTION TO CONVERT PDF TO CSV
def convertPdfToCSV():
    convert_into_by_batch("./", output_format="csv", pages="all")
    


#FUNCTION FOR EXTRACTING SPECIFIC ROWS FROM A CSV FILE.
def extractCsvRows():
    try:
        for i in letters:
            with open(f"CSV/EVSU-College-Admission-Application-Result-SY-2021-2022-{i.upper()}.csv", "r") as file:
                reader = csv.reader(file)
                rows = []
                for row in reader:
                    rows.append(row)

            no_of_BSIT = []
            num = 0
            with open("NumberOfBSITPassers.txt", "a") as f:
                for i in rows:
                    if "BSIT" in i and "MAIN CAMPUS (Tacloban)" in i:
                        num += 1
                        f.write(f"{num}) {str(i)}\n")
                    else:
                        continue
                f.write("\n")
    except FileNotFoundError:
        print("File Not Found, skipping...")


def main():
    print("Type 1 to download the pdf files")
    print("Type 2 to extract the tables in the pdf files and convert them to CSV")
    print("Type 3 to get the statistics of the passers")
    user_input = input()

    if user_input == 1:
        getPdfFiles()
    elif user_input == 2:
        convertPdfToCSV()
    elif user_input == 3:
        extractCsvRows()
    else: 
        print("Pick between 1 - 3")