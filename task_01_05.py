expenses = int(input('Введите величину расходов, руб.: '))
revenue = int(input('Введите величину доходов, руб.: '))
margin = revenue - expenses
if margin > 0 :
    print (f'Поздравляю, вы получили прибыль {margin} руб.')
    print (f'Рентабельность: {margin / revenue * 100:.2f} %')
    numEmpl = int(input('Введите число сотрудниеов: '))
    print(f'Прибыль на одного сотрудников: {margin / numEmpl:.2f} руб.')
elif margin == 0:
    print(f'Вы ничего не заработали')
else:
    print(f'Вы получили убыток: {margin} руб.')