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

    def run(file_name: str):

        notes = model.NotesHandler(file_name)
        notes.read()
        view = ui.View()
        working = True
        is_saved = True
        view.hello(notes.notes)

        while working:
            command = view.get_command()

            if command == 'exit':
                working = False
                try:
                    if not is_saved and view.get_confirm(): 
                        notes.save()
                        is_saved = True
                        view.report(is_saved)
                except:
                    view.get_confirm()
                
                view.bye()

            if command == 'add':
                view.report(
                    notes.add(view.get_new_note())
                )
                is_saved = False

            if command == 'read':
                view.show_note(notes.notes)

            if command == 'save':
                view.report(notes.save())
                