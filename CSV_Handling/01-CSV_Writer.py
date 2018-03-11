import csv

data = [
    "name,score".split(","),
    "Sachin,89".split(","),
    "Dhoni,67".split(","),
    "Sehwag,109".split(","),
    "Virat,100".split(","),
    "Yuvi,50".split(",")
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for d in data:
        writer.writerow(d)