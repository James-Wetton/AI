import csv
import os
Int = 0
Int2 = 0
rowNumb = 0
Result = 0
Number = 0
Status = False
Status2 = False
Test = str(input("Insert Name \n//"))
Pass = str("Insert \n//")
def Digits():
    global Result
    Result= Int / Int2
with open("AI-datatemplate.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        Int2 = Int2 + 1
        for Data in row:
            Int = Int + 1
            if Status == False:
                Number = Number + 1
            if Test == Data:
                Status = True
Digits()
with open("AI-datatemplate.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if rowNumb == Result:
            for data in row:
                if Number == 0:
                    if Status2 == False:
                        print(data)
                        print(Result)
                        Status2 = True
                    else:
                        None
                else:
                    Number = Number - 1
os.system("pause")
