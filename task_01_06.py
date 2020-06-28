start = int(input('Введите результат первого дня тренировки, в км: '))
result = int(input('Введите требуемый результат, в км: '))
numDay = 1
if start >= result:
    print(f'Дистанция {numDay} км выполнена спортсменом в {numDay}-й день ')
else:
    while start < result:
        start = start * 1.1
        numDay += 1
    print(f'Дистанция {result} км будет выполнена спорстменом на {numDay}-й день')
