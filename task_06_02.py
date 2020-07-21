class Road:
    _norm_mass = 25

    def __init__(self, length, width, thick=5):
        try:
            if float(length) > 0 and float(width) > 0 and float(thick) > 0:
                self._length = length
                self._width = width
                self._thick = thick
                print(f'Создан объект Дорога: \n'
                      f'Длина Дороги: {length}м \n'
                      f'Ширина дороги: {width}м\n'
                      f'Толщина дорожного покрытия: {thick}см')
            else:
                print('Ошибка! Указаны неверные параметры дороги')
        except ValueError:
            print('Ошибка! Указаны неверные параметры дороги')

    def wt_asphalt(self):
        try:
            print(f'Масса требуемого асфальта: '
                  f'{self._length * self._width * self._thick * self._norm_mass / 1000} тонн')
        except AttributeError:
            print('Ошибка! Указаны неверные параметры дороги')


r = Road(5000, 20)
r.wt_asphalt()
