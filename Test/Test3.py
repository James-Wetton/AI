import csv
csvnames = []
def CSV():
    with open("AI-datatemplate.csv","r") as csv_file:
        counter = 0
        csv_reader = csv.reader(csv_file)
        global csvnames
        for line in csv_reader:
            if counter == 0:
                csvnames = line
                counter = counter +1
            else:
                None
                counter = counter +1
CSV()
print(csvnames)