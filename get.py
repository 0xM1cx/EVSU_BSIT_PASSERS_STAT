
# CODE TO DOWNLOAD ALL THE PDF FILES USING THEIR LINKS
# import string

# letters = string.ascii_letters
# for i in letters.upper():
#     with open(f"EVSU-College-Admission-Application-Result-SY-2021-2022-{i}.pdf") as f:
#         print(f)

# CODE TO EXTRACT AND CONVERT THE TABLES OF ALL PDF FILES AND CONVERT THEM TO CSV
# from tabula import convert_into_by_batch
# from tabula import read_pdf

# convert_into_by_batch("./", output_format="csv", pages="all")


#EXTRACTING SPECIFIC ROWS FROM A CSV FILE.
import csv
import string

letters = string.ascii_letters
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
 