import ui
import model
import time
import traceback

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

    def run(notes_base: str):
        notes_cache = []   
        working = True
        # приветствие и: всего в записной книжке len() заметок
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
                
                temp = " "
                print("Текст: ")
                while (ord(temp[len(temp)-1]) != 4):
                    temp = "{in1}\n{in2}".format(
                        in1=temp, 
                        in2=input())
                notes_cache[len(notes_cache)-1].body = temp[:len(temp)-1]

            if command == 'read':
                print(notes_cache[int(input("Введите номер заметки: "))-1])

            if command == 'save':
                try:
                    index = int(input("Введите номер заметки: "))
                    with open(notes_base, 'a') as notes:
                        print(
                            f"{notes_cache[index-1].id};{notes_cache[index-1].head};{notes_cache[index-1].body};{time.strftime('%Y.%m.%d %H:%M', time.localtime(notes_cache[index-1].last_modified))}", 
                            file=notes
                            )
                except:
                    traceback.print_exc()
                    print("Congratulations, you have processed exception in Python")
