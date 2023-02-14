import time

class Note(object):

    id_base = 0

    def __init__(self):
        self.id = 1
        self.head = "Заголовок заметки"
        self.body = "Тело заметки"
        self.last_modified = time.time() #Дата и время создания или последнего редактирования

    # для удаления заметки хорошо
    # def __del__(self):
    #     print('удаляется объект {} класса Worker'.format(self.name))

    # для сохранения заметки в файл или наоборот показать на экране
    
    def __str__(self):
        return f"""
Заголовок: {self.head}
                   
Текст: {self.body}
                    
Изменена: {time.localtime(self.last_edited).tm_mday}.{time.localtime(self.last_edited).tm_mon}.{time.localtime(self.last_edited).tm_year} {time.localtime(self.last_edited).tm_hour}:{time.localtime(self.last_edited).tm_min}
"""