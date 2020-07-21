class Car:
    status = 'car_stop'

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Создан автомобиль {self.name}, цвет - {self.color}')

    def go(self):
        if self.status == 'car_stop':
            print(f'Автомобиль {self.name} начал движение со скоростью {self.speed}км/ч')
            self.status = 'car_mov'
        else:
            print(f'Автомобиль {self.name} уже двигается.')

    def stop(self):
        if self.status == 'car_mov':
            print(f'Автомобиль {self.name} остановился.')
        else:
            print(f'Автомобиль {self.name} не может быть остановлен, т.к. не начал движение')

    def show_speed(self):
        if self.status == 'car_mov':
            print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.name} - 0 км/ч')

    def turn(self, direction):
        if self.status == 'car_mov':
            print(f'Автомобиль {self.name} повернул {direction}')
        else:
            print(f'Автомобиль {self.name} не может повернуть, т.к. не начал движение')


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if self.status == 'car_mov' and self.speed <= self.max_speed:
            print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')
        elif self.status == 'car_mov' and self.speed > self.max_speed:
            print(f'Скорость автомобиля {self.name} - {self.speed} км/ч \n'
                  f'Зафикисровано превышение скорости на {self.speed - self.max_speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.name} - 0 км/ч')


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if self.status == 'car_mov' and self.speed <= self.max_speed:
            print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')
        elif self.status == 'car_mov' and self.speed > self.max_speed:
            print(f'Скорость автомобиля {self.name} - {self.speed} км/ч \n'
                  f'Зафикисровано превышение скорости на {self.speed - self.max_speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.name} - 0 км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


class SportCar(Car):
    pass


separator = f'{"-" * 80}'

auto1 = TownCar(30, 'Green', 'Mazda')
auto2 = WorkCar(80, 'Red', 'Lada')
auto3 = PoliceCar(100, 'White', 'Ford')
auto4 = SportCar(250, 'Black', 'Ferrari')

print(separator)
auto2.go()
auto2.show_speed()

print(separator)
auto1.stop()

print(separator)
auto3.go()
auto3.turn('Направо')

print(separator)
auto4.turn('Налево')
