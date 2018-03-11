import csv

def save_data(data):

    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for d in data:
            writer.writerow(d.values())


def read_data():
    data = []
    with open('users.csv') as file:
        reader = csv.reader(file)

        for d in reader:
            data.append(d)

    return data