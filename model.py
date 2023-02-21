import time
import csv
import traceback

"""Создание, изменение, удаление заметок как в кэше-списке словарей, так и в самом файле-источнике"""
class NotesHandler(object):

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.notes = []
        self.file_len = len(self.notes)


    def read(self) -> bool:
        try:
            with open(self.file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    self.notes.append(row)
            self.file_len = len(self.notes)
            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False


    def save(self) -> bool:
        try:
            if self.file_len <= len(self.notes):
                with open(self.file_name, 'w', newline='') as csvfile:
                    fieldnames = ['id', 'header', 'body', 'last_modified']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                    writer.writeheader()
                    writer.writerows(self.notes)
            else:
                with open(self.file_name, 'a', newline='') as csvfile:
                    fieldnames = ['id', 'header', 'body', 'last_modified']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                    for i in range(self.file_len, len(self.notes)):
                        writer.writerow(self.notes[i])
            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False


    def add(self, content: dict) -> bool:
        try:
            self.notes.append({'id': f'{len(self.notes)}'})
            content |= {'last_modified': f'{time.strftime("%d.%m.%Y %H:%M", time.localtime())}'} #я уже знаю, чем мне это грозит. Опять все переделывать, когда дойдет до сортировки по дате. либо как-то заморочитьcя с конвертацией
            self.notes[len(self.notes)-1] |= content

            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False
        

    def change(self, index: int, new_note: dict):
        new_note['last_modified'] = f'{time.strftime("%Y.%m.%d %H:%M", time.localtime())}'
        self.notes[index] = new_note


    def delete(self, index: int):
        self.notes.pop(index)