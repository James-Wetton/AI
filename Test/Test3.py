import csv
csvnames = []
def CSV():
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            for y in x:
                if y == "Username":
                    print(x)
CSV()