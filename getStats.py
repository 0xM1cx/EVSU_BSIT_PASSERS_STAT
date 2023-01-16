import matplotlib


with open("NumberOfBSITPassers.txt", "r") as f:
    NumberOfPassers = []
    lines = f.readlines()
    for i in lines:
        if i == " ":
            print("BlankLine")
        else:
            print(i)
