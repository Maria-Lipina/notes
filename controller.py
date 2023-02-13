import ui
import model

"""Введите одну из доступных команд: add, observe, change, delete:
add - добавить заметку
observe - посмотреть список заметок в памяти
change - отредактировать заметку
delete - удалить заметку
exit - выйти из приложения
manual - руководство по значению команд
save - сохранить заметку в файл-базу
read - прочитать заметку под указанным номером
"""

class Control(object):
    def run():      
        working = True
        while working:
            ui.View.show('Введите одну из доступных команд: add, observe, change, delete, exit, manual, save, read')
            command = input()
            if command == 'exit':
                print('Bye!') #потом это все должно переноситься в методы класса ui
                working = False
            if command == 'add':
                request = ['Введите заголовок']
                answers = ['Введите текст и нажмите CTRL+D']
            if command == 'salary':
                ui.View.show(w.salary)
