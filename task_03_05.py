def is_number(digit):
    """Определяет является ли строка числом"""
    try:
        float(digit)
        return True
    except ValueError:
        return False


result = 0
key_while = None
while key_while != 'Q':
    numb_list = list(input('Введите список чисел разденных пробелом: ').split())
    for i in numb_list:
        if is_number(i):
            result = result + float(i)
        elif i.upper() == 'Q':
            key_while = i.upper()
            break
    print(f'Сумма введенных чисел: {result}')
print('Программа завершена!!!')
