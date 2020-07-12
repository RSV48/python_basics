def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
        yield result


for i in fact(int(input('Введите целое число: '))):
    print(i)
