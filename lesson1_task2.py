# Урок 1 Задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print("Мега софт переведет вам секунды в вид ЧЧ:ММ:СС")
sek = int(input("Введите значение в секундах: "))
if sek <=59:
    print("00 : 00 :", sek)
else:
    min = sek // 60
    sek = sek - (min * 60)
    if min <=59:
        print("00 :", min, ":", sek)
    else:
        chas = min // 60
        min = min - (chas * 60)
        print(chas, ":", min, ":", sek)

