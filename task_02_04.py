originList = list(input('Введите предложение: ').split())
for i, el in enumerate(originList):
    print(f'{i+1} {el[0:10]}')