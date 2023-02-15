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

    def run(file_name: str):
        notes = model.NotesHandler(file_name)
        notes_cache = []   
        working = True
        is_saved = True
        
        # приветствие и: всего в записной книжке len() заметок
        while working:
            
            command = ui.View.get_command()

            if command == 'exit':
                working = False
                ui.View.bye()
                try:
                    if not is_saved and ui.View.get_confirm(): 
                        notes.save()
                except:
                    ui.View.get_confirm()

            if command == 'add':
                
                notes.add()

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
