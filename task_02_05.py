rating = [7,5,5,5,3,2]
digit = None
while not digit:
    digit = input('Введите число: ')
    digit = (float(digit) if digit.isdecimal() else None)
for i, el in enumerate(rating):
    if el < digit :
        rating.insert(i,digit)
        break
    elif i == len(rating)-1:
        rating.append(digit)
        break
print(rating)
