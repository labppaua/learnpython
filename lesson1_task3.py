# Урок 1 Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print("Вы запустили программу гипер калк")
znach = input("Введите значение для расчета от 0 до 9: ")
if int(znach) > 0 and int(znach) < 10:
    res = int(znach) + int(str(znach) + str(znach)) + int(str(znach) + str(znach) + str(znach))
    print("результат сложения", znach, "+", str(znach) + str(znach), "+", str(znach) + str(znach) + str(znach), "=", res)
else:
    print("Число не соответствует диапазону значений!")