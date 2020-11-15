# -*- coding: utf-8 -*-
# Урок 8 задание 7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, vesh, mnim):
        self.vesh = vesh
        self.mnim = mnim

    def __mul__(self, other):
        return Complex(self.vesh * other.vesh, self.mnim * other.mnim)

    def __add__(self, other):
        return Complex(self.vesh + other.vesh, self.mnim + other.mnim)

    def __str__(self):
        return "Complex({}, {})".format(self.vesh, self.mnim)


if __name__ == '__main__':
    c1 = Complex(2, 3.5)
    c2 = Complex(3.5, 4)

    c3 = c1 + c2
    c4 = c1 * c2

    print("c1 is {}".format(c1))
    print("c2 is {}".format(c2))
    print("c3 is {}".format(c3))
    print("c4 is {}".format(c4))