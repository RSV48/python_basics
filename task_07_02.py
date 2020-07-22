from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, sh):
        self.sh = sh
        self.a = 6.5
        self.b = 2
        self.c = 0.3

    @abstractmethod
    def fabric_cons(self):
        pass

    def __add__(self, other):
        return self.fabric_cons + other.fabric_cons


class Coat(Clothes):

    @property
    def fabric_cons(self):
        return round(self.sh / self.a + self.c, 2)


class Suit(Clothes):

    @property
    def fabric_cons(self):
        return round(self.sh * self.b + self.c, 2)


class LengthClot:

    def __init__(self):
        self.coat_length = []
        self.suit_length = []

    def add_coat(self, sh):
        self.coat_length.append(Coat(sh).fabric_cons)

    def add_suit(self, sh):
        self.suit_length.append(Suit(sh).fabric_cons)

    def length_clot(self):
        return round(sum(self.coat_length) + sum(self.suit_length), 2)


print(f'{"-" * 20} Проверка работы класса LengthClot {"-" * 20}')
clot = LengthClot()
clot.add_coat(54)
clot.add_coat(52)
clot.add_suit(180)
clot.add_suit(200)
print(f'Требуемая длинна ткани {clot.length_clot()} м')
print(f'Требуемая длинна ткани на пальто {sum(clot.coat_length)} м')
print(f'Требуемая длинна ткани на костюмы {sum(clot.suit_length)} м')

print(f'{"-" * 20} Проверка работы перегрузки оператра __add __  {"-" * 20} м')
coat1 = Coat(54)
suit1 = Suit(180)
print(f'Требуемая длинна ткани {coat1 + suit1} м')
