import csv

dataSet1 = []
dataSet2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataSet1.append(row)

with open("dwarf.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataSet1.append(row)