class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        try:
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {'wage': wage, 'bonus': bonus}
        except ValueError:
            print('Ошибка! Не верный формат данных!')


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return sum(self._income.values())
        except TypeError:
            print('Ошибка! Не верный формат данных!')


zgd = Position('Andrey', 'Konovalov', 'top Manager', 200000, 1500000)
print(zgd.get_full_name())
print(zgd.get_total_income())
