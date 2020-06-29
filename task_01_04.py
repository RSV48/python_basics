numMax = 0
numUser = int(input('Введите целое положительное число: '))
num = numUser
print(num)
while num != 0:
    if num % 10 > numMax:
        numMax = num % 10
    num = num // 10
print(f'Максимальное число из {numUser}: {numMax}')