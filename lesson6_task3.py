
# -*- coding: utf-8 -*-
# Урок 6 задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


from typing import Dict, Any


class Worker:
    _income: Dict[str, Any]

    def __init__(self, name, surname, position, incomes={}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = incomes

    def get_wage(self):
        return self._income.get("wage", 0)

    def get_bonus(self):
        return self._income.get("bonus", 0)


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        d = {"wage": wage, "bonus": bonus}
        super().__init__(name, surname, position, d)

    def get_position(self):
        return "{}".format(self.position)

    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()

    def print_info(self):
        print("Staff: {} - position: {}\nTotal income: {}".format(self.get_full_name(), self.get_position(),
                                                                   self.get_total_income()))


if __name__ == '__main__':
    boss = Position("Ivanov", "Ivan", "Boss", 123, 256)
    empl = Position("Petrov", "Petr", "Empl", 222, 333)
    tsar = Position("Putin", "Vova", "Tsar", 1, 0)
    boss.print_info()
    empl.print_info()
    tsar.print_info()