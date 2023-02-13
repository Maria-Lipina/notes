class Worker(object):
    name = ""
    salary = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def method(self):
        print(f'{self.name} && {self.salary}')

    def __del__(self):
        print('удаляется объект {} класса Worker'.format(self.name))
