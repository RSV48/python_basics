from functools import reduce


def multiply(el1, el2):
    return el1 * el2


print(reduce(multiply, [i for i in range(100, 1001) if i % 2 == 0]))
