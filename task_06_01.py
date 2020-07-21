import time
import itertools


class TrafficLight:
    # атрибуты класса
    __color = {'Красный': ['\r\033[41m', 7],
               'Желтый': ['\r\033[0m\t\033[43m', 2],
               'Зеленый': ['\r\033[0m\t\t\033[42m', 7],
               'Желтый2': ['\r\033[0m\t\033[43m', 2]}

    def running(self):
        for el in itertools.cycle(self.__color.values()):
            print(f'{el[0]}   ', end="")
            time.sleep(el[1])


a = TrafficLight()
a.running()
