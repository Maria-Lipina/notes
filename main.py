# from controller import Control

# Control.run('notebook.csv')


import csv
import time

notes = []

with open('notebook.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    notes.append(row)

for i in notes:
    print(i)

try:
    notes.sort(key=lambda x: time.mktime(time.strptime("%d.%m.%Y %H:%M",x['last_modified'])), reverse=True)
except ValueError:
    pass

print('----')
for i in notes:
    print(i)

# sort_prepare = {}
# for i in range(len(notes)):
#     sort_prepare[i] = time.mktime(time.strptime(notes[i]['last_modified'], "%d.%m.%Y %H:%M"))

# print('------')
# print(sort_prepare) #{0: 1676990640.0, 1: 1676986440.0, 2: 1676658600.0, 3: 1676662200.0, 4: 1645507800.0, 5: 1645513200.0} len = 6

# def max(being_sorted: dict, sorted: list): 
#     max_value = -1.0
#     for key in being_sorted:
#         if max_value <= being_sorted[key]:
#             max_value = being_sorted[key]
#             max_key = key
#             print(max_key)
#             print(max_value)
    # sorted.append(notes[max_key])
    # print('------')
    # print(sorted)
    # del being_sorted[max_key]
    # print('------')
    # print(being_sorted)
    
    # if len(being_sorted) > 0: max(being_sorted, sorted_keys)


# sorted = []
# max(sort_prepare, sorted)

# lm = '21.02.2023 17:44'
# for_sort = time.mktime(time.strptime(lm, "%d.%m.%Y %H:%M"))
# print(time.strftime("%d.%m.%Y %H:%M", time.localtime(for_sort)))

