import ui
import model

class Control(object):
    def run():
        ui.View.show('Введите параметры рабочего')

        w = model.Worker(input(), int(input()))
        
        ui.View.show('Введите одну из доступных команд: exit, name, salary')
        working = True
        while working:
            command = input()
            if command == 'exit':
                del w
                print('Bye!')
                working = False
            if command == 'name':
                ui.View.show(w.name)
            if command == 'salary':
                ui.View.show(w.salary)
