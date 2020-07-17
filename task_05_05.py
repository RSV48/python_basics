import random
from datetime import datetime as dt


def record_file(list_str, name_file=f'txt_{dt.today().strftime("%Y-%m-%d-%H.%M.%S")}'):
    """Запись списка строк в файл"""
    with open(name_file, 'w', encoding='utf-8') as txt:
        txt.writelines(list_str)


def pars_file(name_file):
    """Парсинг текстового файла"""
    with open(name_file, 'r', encoding='utf-8') as txt:
        return [i.split() for i in txt.readlines()]


num_list = [str((random.randint(1, 1000))) for el in range(1, 100)]
record_file(' '.join(num_list), 'text_5.txt')

print(f'Сумма значений в файле = {sum([int(el) for el in pars_file("text_5.txt")[0]])}')

