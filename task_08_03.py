class Digit(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def math(digit):
        try:
            int(digit)
            return True
        except ValueError:
            try:
                float(digit)
                return True
            except ValueError:
                try:
                    complex(digit)
                    return True
                except ValueError:
                    return False


digit_list = []
while True:
    num = input("Введите число: ")
    try:
        if num == 'stop':
            print(digit_list)
            break
        elif Digit.math(num):
            digit_list.append(num)
        else:
            raise Digit('Введено не число')
    except Digit as err:
        print(err)
