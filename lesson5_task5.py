# -*- coding: utf-8 -*-
# Урок 5 задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print("Введите разные числа разделенные пробелами")
with open("out_file_task5.txt", "w") as out_file:
    data = input()
    out_file.writelines(data)

with open("out_file_task5.txt", "r") as in_file:
    print("Вывод содержания созданного файла")
    cont = in_file.read()
    print(cont)
# для суммирования проще использовать sum но я взял кусок из предыдущих заданий, должен же он хоть раз пригодиться
    val = cont.split()
#    print(val)
    c = 0
    b = len(val)
    i = 0
    while i < b:
        c = c + float(val[i])
        i = i + 1
    print(c)

