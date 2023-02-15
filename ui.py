class View(object):

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

    
    def get_number(self, notes: list):
        num = int(input("Введите номер заметки: "))-1
        if num >= len(notes): self.get_number(notes)
        else: return num

    def show_note(self, notes: list):
        print(notes[self.get_number(notes)])