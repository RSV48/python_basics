from itertools import count
from itertools import cycle

try:
    digit = int(input('Введите целое число: '))
except ValueError:
    print('Введено не корреткное значение. Работа скрипта завершена.')

str_line = input('Введите строку: ')

# ------------------- Подзадача А ----------------------------

iteratorA = (i for i in count(digit))

# ------------------- Подзадача Б ----------------------------

iteratorB = (i for i in cycle(str_line))

# ------------------- Подзадача * ----------------------------

iteratorAB = (el1 * el2 for el1 in count(abs(digit)) for el2 in cycle(str_line))

# Вывод результатов

print(f'{"-" * 20} Результат работы ИТЕРАТОРА А {"-" * 20}')
for el in range(abs(digit)):
    print(next(iteratorA))

print(f'{"-" * 20} Результат работы ИТЕРАТОРА B {"-" * 20}')
for el in range(abs(digit)):
    print(next(iteratorB))

print(f'{"-" * 20} Результат работы ИТЕРАТОРА АB {"-" * 20}')
for el in range(abs(digit)):
    print(next(iteratorAB))

print(f'{"-" * 10} Работа скрипта завершена. Бесконечных циклов нет.{"-" * 10}')
