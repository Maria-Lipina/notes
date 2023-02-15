import time
import csv

"""Создание, изменение, удаление заметок как в кэше-списке словарей, так и в самом файле-источнике"""
class NotesHandler(object):

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.notes = []
        self.file_len = len(self.notes)


    def read(self):
        with open(self.file_name, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self.notes.append(row)
        self.file_len = len(self.notes)


    def save(self):
        if self.file_len <= len(self.notes):
            with open(self.file_name, 'w', newline='') as csvfile:
                fieldnames = ['header', 'body', 'last_modified']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                writer.writeheader()
                writer.writerows(self.notes)
        else:
            with open(self.file_name, 'a', newline='') as csvfile:
                fieldnames = ['header', 'body', 'last_modified']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                for i in range(self.file_len, len(self.notes)):
                    writer.writerow(self.notes[i])

    def add(self, content: dict):
        content |= {'last_modified': f''}
        self.notes.append(content)