# Урок 8 задане 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyExc(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    val1 = int(input("Введите положительное число: "))
    val2 = int(input("Введите положительное число: "))

    res = 0
    try:
        if val2 == 0:
            raise MyExc("Division by zero")
        else:
            res = val1 / val2
    except MyExc as ex:
        print(ex)
    else:
        print("Result is: {}".format(res))