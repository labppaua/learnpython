# -*- coding: utf-8 -*-
# Урок 5 задание 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

trans_rus = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
out_file = []
with open("file_task4.txt", "r") as in_file:
    print("Вывод содержания файла до изменений")
    cont = in_file.read().split("\n")
    print(cont)
    in_file.seek(0)
    for i in in_file:
        i = i.split(" ", 1)
#        print(i)
        out_file.append(trans_rus[i[0]] + " " + i[1])

with open("out_file_task4.txt", "w") as file_out:
    file_out.writelines(out_file)

with open("out_file_task4.txt", "r") as in_file:
    print("Вывод содержания файла после изменений")
    cont = in_file.read().split("\n")
    print(cont)