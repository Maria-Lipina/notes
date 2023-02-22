# from controller import Control

# Control.run('notebook.csv')


import csv
import time
import datetime

notes = []

with open('notebook.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        notes.append(row)

for i in notes:
    print(i)           

print('----')

notes.sort(key=lambda x: datetime.datetime.strptime(x['last_modified'], '%d.%m.%Y %H:%M'))
for i in notes:
    print(i)
