listProduct = []
num = 0
compEntry = None
reportName = []
reportPrice = []
reportUnits = []
reportOneUnit = set()

while not compEntry == 'exit':
    num += 1
    print('-' * 20 + f' Ввод параметорв товара {num} ' + '-' * 20)
    nameProduct = input('\nНаименование товара: ')
    priceProduct = float(input('Цена товара: '))
    unitsProduct = int(input('Количество единиц товара: '))
    oneUnit = input('Единицы измерения: ')
    listProduct.append((num, {'name': nameProduct, 'price': priceProduct,
                              'units': unitsProduct, 'oneUnit': oneUnit}))
    print('-' * 20 + f' Ввод параметорв товара {num} завершен ' + '-' * 20)
    compEntry = input('   exit - заврешить работу'
                      '\n   list - вывести отчет'
                      '\n   Нажимите Enter - для продолжения ввода инофрмации о товрах'
                      '\n   Введите команду:  ')
    if compEntry == 'list':
        print('-' * 20 + ' Отчет о наличии товаров ' + '-' * 20)
        for i in listProduct:
            reportName.append(i[1]['name'])
            reportPrice.append(i[1]['price'])
            reportUnits.append(i[1]['units'])
            reportOneUnit.add(i[1]['oneUnit'])
        report = {'Наименование товара': reportName, 'Цена товара': reportPrice,
                  'Количество единиц товара': reportUnits, 'Единицы измерения': list(reportOneUnit)}
        for i, el in report.items():
            print(f'{i}: , {el}')
        print('-' * 20 + ' Конец отчета о наличии товаров ' + '-' * 20)
        compEntry = input('   exit - заврешить работу'
                          '\n   Нажимите Enter - для продолжения ввода инофрмации о товрах'
                          '\n   Введите команду:  ')
