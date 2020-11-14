# -*- coding: utf-8 -*-
# Урок 6 задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed , color , name , is_police = False):
        self.speed = speed
        self.color = color
        self.name  = name
        self.is_police = is_police

    def show_speed(self):
        print("Car speed is {}".format(self.speed))

    def go(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")

    def turn(self, direction):
        print("Car is turned to the {}".format(direction))


class TownCar(Car):
    def __init__(self, speed , color , name , is_police = False):
        super().__init__(speed , color , name , is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Car speed is very high {}".format(self.speed))
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed , color , name , is_police = False):
        super().__init__(speed , color , name , is_police)


class WorkCar(Car):
    def __init__(self, speed , color , name , is_police = False):
        super().__init__(speed , color , name , is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Car speed is very high {}".format(self.speed))
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed , color , name , is_police = True):
        super().__init__(speed , color , name , is_police)


if __name__ == '__main__':
    tc = TownCar(10, "blue", "renault")
    tc.show_speed();
    tc.turn("Left")
    sc = SportCar(20, "white", "renault1")
    sc.show_speed();
    sc.turn("Right")
    wc = WorkCar(30, "green", "renault2")
    wc.show_speed();
    wc.turn("Left")
    pc = PoliceCar(40, "brown", "renault3")
    pc.show_speed();
    pc.turn("Right")
    tcs = TownCar(70, "blue", "renault")
    tcs.show_speed();
    tcs.turn("Right")