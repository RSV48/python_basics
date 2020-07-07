def sum_max(num_1, num_2, num_3):
    """Возвращает  сумму максимальных двух чисел"""
    try:
        el = [num_1, num_2, num_3]
        el = list(map(float, el))
        return sum(el) - min(el)
    except ValueError:
        print(f'Введен не верный аргумент функции: {num_1}, {num_2}, {num_3}')


numbers = []
i = 1
while i < 4:
    number = (input(f'Введите число {i}:'))
    numbers.append(number)
    i += 1
str_num = ', '.join(numbers)
print(f'Сумма максимальных двух чисел из {str_num} равна {sum_max(numbers[0], numbers[1], numbers[2])}')

