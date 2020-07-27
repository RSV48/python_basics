class Date:
    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def dt_digit(cls,dt):
        try:
            return cls.valid_dt(list(map(int, dt.split('-'))))
        except TypeError:
            print('Ошибка в формате даты!')

    @staticmethod
    def valid_dt(dt_list):
        day_month = {28: [2], 30: [4, 6, 9, 11], 31: [1, 3, 5, 7, 8, 10, 12]}
        max_day = False
        for d, m in day_month.items():
            if dt_list[1] in m:
                max_day = d if dt_list[2] % 2 != 0 else d+1
        day = dt_list[0] if 0 < dt_list[0] <= max_day else 'Ошибка!'
        month = dt_list[1] if 1 <= dt_list[1] <= 12 else 'Оишибка!'
        year = dt_list[2] if 1920 <= dt_list[2] <= 2050 else 'Ошибка!'
        print(f'Результат провреки даты:\n'
              f'\tдень:  {day}\n'
              f'\tмесяц: {month}\n'
              f'\tгод:   {year}')


Date.dt_digit('12-02-2020')


