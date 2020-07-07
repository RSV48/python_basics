# ------------------------------ Решение 1 -----------------------------
def ex_func_1(x, y):
    """Возводит число в степень"""
    try:
        return round(abs(x) ** (-abs(y)), 4)
    except TypeError:
        print(f'Введен не верный аргумент функции: {x}, {y}')


# ------------------------------ Решение 2 -----------------------------

def ex_func_2(x, y):
    """Возводит число в степень"""
    try:
        arg = abs(x)
        for i in range(1, abs(y)):
            arg *= abs(x)
        return round(1 / arg, 4)
    except TypeError:
        print(f'Введен не верный аргумент функции: {x}, {y}')

print(ex_func_1(8, 3))
print(ex_func_2(8, 3))
