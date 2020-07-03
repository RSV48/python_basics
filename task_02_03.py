month = None
while not month:
    month = input('Введите месяц - целое число от 1 до 12: ')
    month = (int(month) if month.isdigit() and int(month) <= 12 else None)
# ----------------- Решение 1 ------------------------
print('-' * 20 + 'Решение 1' + '-' * 20 )
season = ['Зима', 'Весна', 'Лето', 'Осень']
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print(f'{month}-й месяц - {season[0]}')
elif month in spring:
    print(f'{month}-й месяц - {season[1]}')
elif month in summer:
    print(f'{month}-й месяц - {season[2]}')
elif month in autumn:
    print(f'{month}-й месяц - {season[3]}')

# ----------------- Решение 2 ------------------------
print('-' * 20 + 'Решение 2' + '-' * 20 )
seasonDict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for i in seasonDict:
    if month in seasonDict[i]:
        print(f'{month}-й месяц - {i}')
        break
