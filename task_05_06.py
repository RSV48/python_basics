def pars_file(name_file):
    """Парсинг текстового файла"""
    with open(name_file, 'r', encoding='utf-8') as txt:
        return [i.split() for i in txt.readlines()]


def el_dict(str_dict):
    """Создает словарь предметов со списками записей"""
    result = {}
    for i in str_dict:
        result[i[0]] = i[1:]
    return result


def sum_list(list_str):
    """Суммирует количество часов в записях"""
    num_list = [str(el) for el in range(0, 10)]
    sum_digit = 0
    for i in list_str:
        digit = ''.join([sym for sym in i if sym in num_list])
        sum_digit += int(digit) if digit else 0
    return sum_digit


new_dict = el_dict(pars_file('text_6.txt'))
for key, val in new_dict.items():
    new_dict[key] = sum_list(val)
print(new_dict)