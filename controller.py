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
        notes_cache = []   
        working = True
        while working:
            ui.View.show('Введите одну из доступных команд: add, observe, change, delete, exit, manual, save, read')
            command = input()

            if command == 'exit':
                print('Bye!') #потом это все должно переноситься в методы класса ui
                working = False
            
            if command == 'add':
                notes_cache.append(model.Note())
                print(f'{len(notes_cache)} + сколько всего заметок')


                notes_cache[len(notes_cache)-1].head = input("Заголовок: ")
                
                notes_cache[len(notes_cache)-1].body = "\n"
                print("Текст: ")
                while (ord(
                    notes_cache[len(notes_cache)-1]
                    .body[len(notes_cache[len(notes_cache)-1].body)-1]
                    ) != 4):

                    notes_cache[len(notes_cache)-1].body = "{in1}\n{in2}".format(
                        in1=notes_cache[len(notes_cache)-1].body, 
                        in2=input())
            
            if command == 'read':
                print(notes_cache[0])