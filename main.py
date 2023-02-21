# from controller import Control

# Control.run('notebook.csv')
import datetime

# import csv

# notes = []

# with open('notebook.csv', 'r', newline='') as csvfile:
#                 reader = csv.DictReader(csvfile, delimiter=';')
#                 for row in reader:
#                     notes.append(row)

lm = '21.02.2023 17:44'

import datetime
import time

for_sort = time.mktime(time.strptime(lm, "%d.%m.%Y %H:%M"))
print(time.strftime("%d.%m.%Y %H:%M", time.localtime(for_sort)))

