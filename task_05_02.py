def sum_word(name):
    """Подсчитывает и выводит количество строк, слов в файле и количество слов в каждой строке"""
    with open(name, 'r', encoding='utf-8') as txt:
        txt_list = txt.readlines()
        print(f'Количество строк в файле: {len(txt_list)}')
        num_word = [len(i.split()) for i in txt_list]
        print(f'Количество слов в файле: {sum(num_word)}')
        for wLine in range(1, len(num_word) + 1):
            print(f'Число слов в строке {wLine}: {num_word[wLine - 1]}')


sum_word('text_2.txt')
