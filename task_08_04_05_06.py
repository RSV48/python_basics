from abc import ABC, abstractmethod
from itertools import count


class Digit(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def math(digit):
        try:
            int(digit)
            return True
        except:
            return False


class OffTech(ABC):

    def __init__(self, speed, paper_size):
        self.speed = speed
        self.paper_size = paper_size

    @abstractmethod
    def reg(self):
        pass


class Printer(OffTech):
    def __init__(self, speed=100, paper_size='A4', color=False):
        super().__init__(self, speed)
        self.speed = speed
        self.paper_size = paper_size
        self.color = color

    def reg(self):
        return ['Printer', self.paper_size, self.speed, self.color]


class Scanner(OffTech):
    def __init__(self, speed, paper_size='A4', stream_scan=False):
        super().__init__(self, speed)
        self.speed = speed
        self.paper_size = paper_size
        self.stream_scan = stream_scan

    def reg(self):
        return ['Scanner', self.paper_size, self.speed, self.stream_scan]


class Xerox(OffTech):
    def __init__(self, speed, paper_size='A4', color=False, stream_scan=False, ):
        super().__init__(self, speed)
        self.speed = speed
        self.paper_size = paper_size
        self.stream_scan = stream_scan
        self.color = color
        self.stream_scan = stream_scan

    def reg(self):
        return ['Xerox', self.paper_size, self.speed, self.stream_scan, self.color]


class Wh:

    def __init__(self):
        """В качестве контенеров использованы словари и списки.
        Было бы правилнее использовать запрос в базу данных, но мы это еще не проходили
        Или записывать и читать все из файлов, но на это не хватило времени """
        self.location = {}
        self.t_dict = {}
        self.inv_num = (i for i in count(1))
        self.dep = ['Списать', 'Склад', 'Отдел 1', 'Отдел 2']
        self.object = ['Принтер', 'Сканер', 'Ксерокс']

    @staticmethod
    def listing(param):
        max_i = 0
        for i in range(1, len(param) + 1):
            print(f'{i}. {param[i - 1]}')
            max_i = i
        return max_i

    def mov(self, inv_num):
        """Функция перемещает объект из одного подразддения в другое"""
        if inv_num in self.location.keys():
            max_i = Wh().listing(self.dep)
            n = max_i + 1
            while not Digit.math(n) or int(n) > max_i or int(n) <= 0:
                try:
                    n = input(f'Выберите куда переместить объект. Текущее расположение: {self.location[inv_num]}:')
                    if not Digit.math(n):
                        raise Digit("Ошибка! Введите целое число")
                    elif int(n) > max_i or int(n) <= 0:
                        raise Digit("Ошибка. Номер подразденения не соовтествует ни одному подразделению")
                    else:
                        self.location[inv_num] = self.dep[int(n) - 1]
                except Digit as err:
                    print(err)
        else:
            print(f'Оборудование с инвентаризационным номером {inv_num} не зарегистрированно или Списано')

    def add_dep(self):
        """Функция добавляет подраздление"""
        Wh().listing(self.dep)
        name = input('Введите наименование подразделения:')
        if not name in self.dep:
            self.dep.append(name)
            print(f'Отдел {name} добавлен')
        else:
            print('Такой отдел уже существует')

    # Функции регистрации новых объектов и размещение их на складе

    def add_printer(self, num, speed, paper_size='A4', color=False):
        """Добавление новых притеров, num - количество новых принтеров"""
        if Digit.math(num) and Digit.math(speed):
            for i in range(0, num):
                n = next(self.inv_num)
                self.t_dict.setdefault(f'Printer_{n}', Printer(speed, paper_size, color).reg())
                self.location.setdefault(f'Printer_{n}', self.dep[1])
        else:
            print('Количество принеторов и скорость печати должны быть целыми положительными числами ')

    def add_scanner(self, num, speed, paper_size='A4', stream_scan=False):
        if Digit.math(num) and Digit.math(speed):
            for i in range(0, num):
                n = next(self.inv_num)
                self.t_dict.setdefault(f'Scanner_{n}', Scanner(speed, paper_size, stream_scan).reg())
                self.location.setdefault(f'Printer_{n}', self.dep[1])
        else:
            print('Количество сканеров и скорость сканирования должны быть целыми положительными числами ')

    def add_xerox(self, num, speed, paper_size='A4', color=False, stream_scan=False):
        if Digit.math(num) and Digit.math(speed):
            for i in range(0, num):
                n = next(self.inv_num)
                self.t_dict.setdefault(f'Xerox_{n}', Xerox(speed, paper_size, color, stream_scan).reg())
                self.location.setdefault(f'Printer_{n}', self.dep[1])
        else:
            print('Количество ксерокосов и скорость копирования должны быть целыми положительными числами ')


warehouse = Wh()

warehouse.add_printer(10, 100, 'A3', True)
warehouse.add_scanner(2, 100, 'A4', False)
warehouse.add_xerox(4, 500, 'A3', True, True)
warehouse.add_dep()
warehouse.mov('Printer_5')
print(warehouse.t_dict)
print(warehouse.location)
