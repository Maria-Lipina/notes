import datetime
import time
from controller import Control

import csv
addition = "какая-то строка\r\n"

with open('eggs.csv', 'r+', newline='') as csvfile:
    content = []
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        content.append(row)
    # content = csvfile.readlines()
    print(content)
    print(content[0][1])
    # with open('notebook.csv', 'a', newline='') as csvfile1:
    #     for n in content:
    #         csvfile1.write(n)
    #     csvfile1.write(addition)
    #     csvfile1.writelines(content)

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# Control.run('notebook.csv')
