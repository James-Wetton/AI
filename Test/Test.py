import csv


"""for loops Isolate each line into a list"""
with open("E:\James\AI\Test\Test.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
    csv_file.close


"""Prints Second Row"""
with open("E:\James\AI\Test\Test.csv","r") as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    for line2 in csv_reader2:
        print(line2[1])


"""Replaces delmiter with '-'"""
with open("E:\James\AI\Test\Test.csv","r") as csv_file3:
    csv_reader3 = csv.writer(csv_file3,delimiter ="-")