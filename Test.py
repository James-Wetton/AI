import csv
import os
User = str(input("Insert Name \n</ "))
Pass = ""
def getPass():
    dataCounter = 1
    rowCounter = 0
    limitSwitch1 = False
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for data in row:
                if data == User:
                    limitSwitch1 = True
                elif data != User and limitSwitch1 == False:
                    dataCounter = dataCounter + 1
                else:
                    None
        csv_file.close
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            rowCounter = rowCounter + 1
            if rowCounter == 2:
                for data in row:
                    if dataCounter == 0:
                        global Pass
                        Pass = data
                    else:
                        dataCounter = dataCounter - 1
getPass()
print(Pass)
os.system("pause")
