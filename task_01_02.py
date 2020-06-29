timeSec = int(input('Введите время в секундах: '))
numHours = timeSec // 3600
numMin = (timeSec % 3600) // 60
numSec = timeSec % 60
if numHours < 10:
    numHours = '0' + str(numHours)
if numMin < 10:
    numMin = '0' + str(numMin)
if numSec < 10:
    numSec = '0' + str(numSec)
print(f'{timeSec} секунд в формате чч:мм:сс: {numHours}:{numMin}:{numSec}')
