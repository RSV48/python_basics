expenses = int(input('Введите величину расходов: '))
revenue = int(input('Введите величину доходов: '))
margin = revenue - expenses
if margin > 0 :
    print (f'Поздравляю, вы получили прибыль {margin}')
    print (f'Рентабельность: {(margin / revenue * 100):2f} %')
    numEmpl = int(input('Введите число сотрудниеов: '))
    print(f'Прибыль на одного сотрудников: {margin / numEmpl:2f}')
elif margin == 0:
    print(f'Вы ничего не заработали')
else:
    print(f'Вы получили убыток: {margin}')