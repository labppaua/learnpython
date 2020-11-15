# -*- coding: utf-8 -*-
# Урок 8 задание 4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Sklad:
    def __init__(self, name: str):
        self.name = name
        self.polki = [1, 2, 3, 4, 5, 6]
        self.positions = [1, 2, 3, 4, 5, 6]
        self.items = {}
        self.departments = ["HR", "IT"]

    def add_to_sklad(self, device, pos, polka):
        self.items[device.serial_number] = {"info": device, "polka": polka, "pos": pos}

    def remove_from_sklad(self, device, department):
        dev = self.items.get(device.serial_number)
        if dev is None:
            print("Device with S/N {} is not found".format(device.serial_number))
        else:
            dev.department = department
            del self.items[device.serial_number]

    def print_dev_info(self, device):
        dev = self.items.get(device.serial_number)
        if dev is None:
            print("Device with S/N {} is not found".format(device.serial_number))
        else:
            dev_info = dev.get("info")
            print("Device info:\n\tType: {}\n\tModel: {}\n\tS/N: {}\n\tDate of: {}\n".format(dev_info.type_of,
                                                                                             dev_info.model,
                                                                                             dev_info.serial_number,
                                                                                             dev_info.date_of))
            print("Polka: {}\nPos:   {}\n".format(dev.get("polka"), dev.get("pos")))
class Orgtechnika:
    def __init__(self, type_of: str, model: str, serial_number: str, date_of: str, department = ""):
        self._type_of = type_of
        self._model = model
        self._serial_number = serial_number
        self._date_of = date_of
        self._department = department

    @property
    def type_of(self):
        return self._type_of

    @property
    def model(self):
        return self._model

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def date_of(self):
        return self._date_of

    @property
    def department(self):
        return self._department


class Printer(Orgtechnika):
    def __init__(self, model: str, serial_number: str, date_of: str,  department: str, printer_type_network: bool):
        super().__init__("Принтер", model, serial_number, date_of, department)
        self.printer_type_network = printer_type_network

    def is_network(self):
        return self.printer_type_network


class Xerox(Orgtechnika):
    def __init__(self, model: str, serial_number: str, date_of: str, department, resource: int):
        super().__init__("Ксерокс", model, serial_number, date_of, department)
        self.resource = resource

    def resource(self):
        return self.resource


if __name__ == '__main__':
    sklad = Sklad("Главный")
    p = Printer("Brother", "111", "11-11-2020", "IT", False)
    sklad.add_to_sklad(p,1,1)
    sklad.print_dev_info(p)