from datetime import datetime as dt


def tr_lat(trans_list):
    """Переводчик"""
    table = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    translation = str.maketrans(table)
    for i in range(len(trans_list)):
        try:
            trans_list[i][0] = (trans_list[i][2].translate(translation))
        except IndexError:
            trans_list[i].append('No translate')
            continue
    return (f"{' '.join(el)} \n" for el in trans_list)


def pars_file(name_file):
    """Парсинг текстового файла"""
    with open(name_file, 'r', encoding='utf-8') as txt:
        return [i.split() for i in txt.readlines()]


def record_file(list_str, name_file= f'txt_{dt.today().strftime("%Y-%m-%d-%H.%M.%S")}'):
    """Запись списка строк в файл"""
    with open(name_file, 'w', encoding='utf-8') as txt:
        txt.writelines(list_str)


record_file(tr_lat(pars_file('text_4.txt')))
