def int_func(word):
    for i in word:
        if 97 > ord(i) < 122:
            return False
    return word.title()


result = []
while not result:
    word_list = input('Ведите строку латинскими буквами в нижем регистре, разделив слова пробелами: ').split()
    for word in word_list:
        if int_func(word):
            result.append(int_func(word))
        else:
            result.clear()
            print(f'Строка {" ".join(word_list)} включат в себя символы отличные от латинских букв в нижнем регистре')
            break
print(f'Программа заврешена {" ".join(result)}')
