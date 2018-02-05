import os
import csv
counter = 0
names = []

def FindName():
    with open("AI-datatemplate.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            global counter
            if counter == 0:
                global names
                names = line
                counter = counter + 1
                print("A")
            else:
                None
                print("B")
FindName()
os.system("pause")