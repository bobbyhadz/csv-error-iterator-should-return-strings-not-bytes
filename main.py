import csv


with open('employees.csv', 'rt', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    for row in csv_reader:
        print(row)
