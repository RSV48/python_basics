print('Давайте определим Ваш возвраст!!!')
fio = input ('Введите Ваши - Имя Отчество: ')
birthYear = int(input (f'{fio}, пожалуйста введите год Вашего рождения: '))
curYear = int(input (f'{fio}, пожалуйста введите текущий год: '))
if curYear > birthYear:
    print(f'{fio}, вам сейчас {curYear - birthYear} полных лет')
elif curYear == birthYear:
    print(f'{fio}, вам сейчас менее года')
else:
    print(f'{fio}, вы еще не родились')
