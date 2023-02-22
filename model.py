import datetime
import time
import csv
import traceback


class NotesHandler(object):
    """Создание, изменение, удаление заметок, загрузка данных из файла (передается в конструкторе), сохранение в файл"""

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.notes = []
        self.file_len = len(self.notes)
        self.glossary = {}


    def load(self) -> bool:
        try:
            with open(self.file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    self.notes.append(row)
            self.file_len = len(self.notes)
            self.date_sort()

            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False


    def save(self) -> bool:
        self.date_sort()
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
            self.notes.append({'id': f'{len(self.notes)+1}'})
            content |= {'last_modified': f'{time.strftime("%d.%m.%Y %H:%M", time.localtime())}'}
            self.notes[len(self.notes)-1] |= content
            self.glossary[str(len(self.notes))] = len(self.notes)-1
            print(self.glossary)
            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False
        

    def change(self, new_note: dict):
        try:
            for i in self.notes:
                print(i)
            print('----')
            
            new_note['last_modified'] = f'{time.strftime("%d.%m.%Y %H:%M", time.localtime())}'
            self.notes[self.glossary[new_note['id']]] = new_note
            
            for i in self.glossary:
                print(self.notes[self.glossary[i]])
            
            self.date_sort()
            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False

    def delete(self, id: str):
        try:
            self.notes.pop(self.glossary[id])
            del self.glossary[id]
            self.date_sort()
            print(self.glossary)
            return True
        except:
            traceback.print_exc(file=open('log.txt', 'w'))
            return False
        
        


    def date_sort(self):
        self.notes.sort(key=lambda x: datetime.datetime.strptime(x['last_modified'], '%d.%m.%Y %H:%M'))
        for i in range(len(self.notes)):
            self.glossary[self.notes[i]['id']] = i