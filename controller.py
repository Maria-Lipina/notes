import ui
import model


class Control(object):
    """Обработка запросов от пользователя, делегирование задач другим элементам приложения. Под аргументом file_name передается путь к хранилищу заметок в формате csv"""

    def run(file_name: str):

        notes = model.NotesHandler(file_name)
        notes.load()
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
                        is_saved = notes.save()
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
                view.show_note(notes.notes, notes.glossary)


            if command == 'save':
                is_saved = notes.save()
                view.report(is_saved)

            if command == 'change':
                view.report(notes.change(
                    view.get_changed_note(notes.glossary)
                ))
                is_saved = False

            if command == 'delete':
                view.report(notes.delete(view.get_id(notes.glossary)))
                is_saved = False

            if command == 'manual':
                view.show_manual()

            if command == 'observe':
                notes.date_sort()
                view.show_notes(notes.notes)
