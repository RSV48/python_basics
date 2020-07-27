class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = input("Введите числитель: ")
div = input("Введите знаменатель: ")

try:
    num = int(num)
    div = int(div)
    if div == 0:
        raise OwnError("Ошибка! Деление на ноль")
except ValueError:
    print("Введено не число")
except OwnError as err:
    print(err)
else:
    print(f"{num} / {div} = {num / div}")
