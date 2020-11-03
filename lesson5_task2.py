# -*- coding: utf-8 -*-
# Урок 5 задание 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

in_f = open("file_task2.txt")
cont = in_f.read()
print(cont, "\n")
in_f.seek(0)
line = 0
for i in in_f:
    line = line + 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print("в строке", line, "слов", word)
print("строк в данном файле", line)
in_f.close()