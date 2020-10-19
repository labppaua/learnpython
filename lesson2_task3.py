# Урок 2 задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = input("Введите значение месяца цыфрами от 1 до 12 ")

def is_digit(month):
    if month.isdigit():
        return True
    else:
        try:
            float(month)
            return True
        except ValueError:
            return False
if is_digit(month) != True:
    print("то, что вы ввели не похоже на цифры")
else:
    month = float(month)
    def isInt(month):
        return int(month) == float(month)
    if isInt(month) == False:
        print("вы ввели не целое число, сомневаюсь, что бывают дробные месяцы")
    else:
        if month > 0 and month < 13:
            month = int(month)
            list_seazon = ("зима", "весна", "лето", "осень")
            list_month = {1:"январь", 2:"февраль", 3:"март", 4:"апрель", 5:"май", 6:"июнь", 7:"июль", 8:"август", 9:"сентябрь", 10:"октябрь", 11:"ноябрь", 12:"декабрь"}
            print(month, "месяц - это", list_month[month])
            if month == 12 or 1<=month<3:
                print("однако", list_seazon[0])
            elif 3<=month<6:
                print("это", list_seazon[1])
            elif 6 <= month < 9:
                print("яхху - это", list_seazon[2])
            elif 9 <= month < 12:
                print("эх это", list_seazon[3])
        else:
            print("не бывает такого месяца")
