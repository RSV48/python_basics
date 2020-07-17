def pay(name):
    """Подсчитывает среднюю заработную плату"""
    with open(name, 'r', encoding='utf-8') as txt:
        try:
            txt_list = txt.readlines()
            name_pay = [i.split() for i in txt_list]
            sum_pay = 0
            for el in name_pay:
                sum_pay += float(el[1])
                if float(el[1]) < 20000:
                    print(el[0])
            print(f'Средений доход сотрудников составляет: {sum_pay / len(txt_list)}₽')
        except ValueError:
            print(f'В строке {el} допущена ошибка!')


pay('text_3.txt')
