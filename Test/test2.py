import csv
with open("E:\James\AI\Test\Test.csv","r") as csv_file:
    counter = 0
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if counter == 1:
            print(line)
        else:
            counter = counter + 1