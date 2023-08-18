import csv

with open('insurance.csv') as file:
    file_reader = csv.reader(file, delimiter=',')
    for row in file_reader:
        print(row)