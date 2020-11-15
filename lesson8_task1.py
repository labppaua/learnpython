# Урок 7 задание 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    data: str

    def __init__(self, data: str):
        Data.data = data

    @staticmethod
    def test_data(values: list):
        if len(values) < 3:
            print("Wrong data {}".format(values))
        else:
            month = values[1]
            year = values[2]
            if month < 1 or month > 12:
                print("Wrong month number: {}".format(month))
                return
            if year > 2090 or year < 1900:
                print("Wrong year number: {}".format(year))
                return
            print("Day: {}\nMonth: {}\nYear: {}\n".format(values[0], values[1], values[2]))

    @classmethod
    def parse_data(cls):
        values = [int(i) for i in cls.data.split("-")]
        Data.test_data(values)


if __name__ == '__main__':
    d1 = Data("11-12-2000")
    Data.parse_data()
