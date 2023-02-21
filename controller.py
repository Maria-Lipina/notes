import ui
import model


class Control(object):
    """Класс для передачи запросов от пользователя другим элементам приложения, в том числе обращения к хранилищу заметок в файле, путь к которому передан под аргументом @file_name"""

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

            if command == 'change':
                notes.change(
                    view.get_number(notes.notes), view.get_new_note()
                )
                is_saved = False

            if command == 'delete':
                notes.delete(view.get_number(notes.notes))
                is_saved = False

            if command == 'manual':
                view.show_manual()

            if command == 'observe':
                view.show_notes(notes.notes)
