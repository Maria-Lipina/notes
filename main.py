import datetime
import time
from controller import Control

import csv

# addition = {'header':'added by user', 'body':'multiline\note\naas i want', 'last_modified':'12.07.2022 13:30'}
# content = []
# with open('eggs.csv', 'r', newline='') as csvfile:
#     notesreader = csv.DictReader(csvfile, delimiter=';')
#     for row in notesreader:
#         content.append(row)
#     print(content)
#     print(content[1])
#     print(content[1]['body'])

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['header', 'body', 'last_modified']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
#     writer.writeheader()
#     writer.writerows(content)

# with open('names.csv', 'a', newline='') as csvfile:
#     fieldnames = ['header', 'body', 'last_modified']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
#     writer.writerow(addition)


# print("\n-----")
# content.append(addition)
# print(content)
Control.run('notebook.csv')
