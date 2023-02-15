class View(object):
    @staticmethod
    def show(text: str):
        print(f'{text}')
    
    @staticmethod
    def get_command():
        print('Введите одну из доступных команд: add, observe, change, delete, exit, manual, save, read')
        return input()

    @staticmethod
    def get_confirm():
        print('Сохранить изменения в записной книжке? (y\\n)')
        if input() == 'y': return True
        if input() == 'n': return False
        else: return 100 #типа код ошибки. Потом разберусь, что с ними можно сделать

    @staticmethod
    def bye():
        print('Bye!')

    def get_new_note():
        return {'header': input("Введите заголовок: "), 'body': input("Введите текст: ")}
