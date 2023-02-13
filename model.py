import time

class Note(object):
    id = 0
    head = "Заголовок заметки"
    body = "Тело заметки"
    last_edited = time.time() #Дата и время создания или последнего редактирования

    # def __init__(self) -> None:
        #Здесь должны присваиваться значения атрибутам


    # def __del__(self):
    #     print('удаляется объект {} класса Worker'.format(self.name))

# У питона свой toString нашелся!
    # def __str__(self):
    #     return 'Номер[' + str(self.id) + ']'