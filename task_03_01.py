def quotient(num, denom):
    """ Возвращает частное от деления"""
    try:
        return round(float(num) / float(denom),2)

    except ValueError:
        print(f'Введены не корректные аргументы функции: {num_1} или {num_2}')

    except ZeroDivisionError:
        print(f'Ошибка функции! Деление на ноль: {num_1} / {num_2}')


result = None
while result is None:
    num_1 = input('Введите аргумент 1 (число):')
    num_2 = input('Введите аргумент 2 (число):')
    result = quotient(num_1, num_2)

print (f'Результат функции: {num_1} / {num_2} = {result}')
