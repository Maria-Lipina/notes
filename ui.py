class View(object):
    """Запрашивает у пользователя данные для выполнения команды, показывает отчет о выполнении, приветствие и прощание"""

    def hello(self, notes: list):
        print(f"Hello! There are {len(notes)} notes in your notebook")  
    
    
    def get_command(self):
        print('Введите одну из доступных команд: add, observe, change, delete, exit, manual, save, read')
        return input()

    
    def get_confirm(self):
        answer = input('Сохранить изменения в записной книжке? (y\\n)' )
        if answer == 'y': return True
        if answer == 'n': return False
        else: return None


    def bye(self):
        print('Bye!')


    def report(self, status: bool):
        if status: print('Done!')
        else: print("Sorry, something has gone wrong. We`ve collected info and are fixing it")


    def get_new_note(self):
        return {'header': input("Введите заголовок: "), 'body': input("Введите текст: ")}


    def get_changed_note(self, glossary: dict):
        id = self.get_id(glossary)
        return {'id': id, 'header': input("Введите заголовок: "), 'body': input("Введите текст: ")}

    
    def get_id(self, glossary: dict):
        id = input("Введите id заметки: ")
        if id in glossary.keys(): return id
        else: return self.get_id(glossary)


    def show_note(self, notes: list, glossary: dict):
        what_note = self.get_id(glossary)
        print(f"id {notes[glossary[what_note]]['id']}. header: {notes[glossary[what_note]]['header']}\nbody: {notes[glossary[what_note]]['body']}\nlast modified: {notes[glossary[what_note]]['last_modified']}\n\n")


    def show_notes(self, notes: list):
        for note in notes:
            print(f"id {note['id']}. header: {note['header']}\nbody: {note['body']}\nlast modified: {note['last_modified']}\n\n")


    def show_manual(self):
        print(
            """add - добавить заметку
observe - посмотреть список заметок в оперативной памяти. Если вы перед этим добавляли, удаляли или изменяли заметки, то все измененния будут видны здесь
change - отредактировать заметку
delete - удалить заметку
exit - выйти из приложения
manual - руководство по значению команд
save - сохранить изменения в заметках в долговременную память (файл)
read - прочитать заметку под указанным номером
"""
        )