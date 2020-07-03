# Формируем список
originList = list(input('Ведите элементы списка через запятую: ').split(','))
print(f'Введенный список {originList}')
# Преобразуем список, меня местами  занчения элементов
for i in range(0, len(originList), 2):
    originList.insert(i + 1, originList.pop(i))
print(f'Измененный список {originList}')
