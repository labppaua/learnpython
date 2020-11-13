# Урок 6 задание 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    def __init__(self):
        self.__color = ""

    def running(self):
        while self.__color != "Green":
            if self.__color == "":
                self.__color = "Red"
            elif self.__color == "Red":
                self.__color = "Yellow"
            elif self.__color == "Yellow":
                self.__color = "Green"
            self.print_info()

    def print_info(self):
        print("Color is : ", self.__color)
        if self.__color == "Red":
            time.sleep(7)
        elif self.__color == "Yellow":
            time.sleep(2)
        elif self.__color == "Green":
            time.sleep(3)

if __name__ == "__main__":
    tf = TrafficLight()
    tf.running()