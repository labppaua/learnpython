# -*- coding: utf-8 -*-
# Урок 5 задание 1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print("Введите построчно данные, завершая ввод строки нажатием Enter, для завершения ввода нажмите Enter с пустой строкой")
out_f = open("out_file_task1.txt", "w")
while True:
    data = input()
    if data == "":
        break
    out_f.write(data+"\n")
out_f.close()