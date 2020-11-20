# Урок 7 задание 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import abstractmethod


class Clothes:
    @abstractmethod
    def hom_much(self):
        pass


class Palto(Clothes):
    def __init__(self, v):
        self.V = v

    @property
    def clothes_val(self):
        return self.V

    def hom_much(self):
        return self.clothes_val/6.5 + 0.5


class Costum(Clothes):
    def __init__(self, h):
        self.H = h

    @property
    def clothes_val(self):
        return self.H

    def hom_much(self):
        return 2 * self.clothes_val + 0.3


if __name__ == '__main__':
    p = Palto(6.5)
    print("Palto {}".format(p.hom_much()))
    c = Costum(10)
    print("Costum {}".format(c.hom_much()))