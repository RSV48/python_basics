def wf(name):
    """Создает новый файл и записывает в него вводимые строки.
    Если файл существует, выдает ошибку"""
    try:
        txt = True
        with open(name, 'x', encoding='utf-8') as text_1:
            while txt:
                txt = input("Введите текст. Для выхода нажмите Enter: ")
                print(txt, file=text_1)
    except FileExistsError:
        print('Файл с таким именем уже существует')


wf('text_1.txt')
