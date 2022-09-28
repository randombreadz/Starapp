import csv

data = []

with open("dwarf_data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2] = data_point[2].lower()

star_data.sort(key = lambda star_data: star_data[2])

with open("dwarf_data_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

with open("dwarf_data_sorted.csv") as input, open("dwarf_data_sorted1.csv", "w", newline = "") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any (field.strip() for field in row):
            writer.writerow(row)