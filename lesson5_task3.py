# -*- coding: utf-8 -*-
# Урок 5 задание 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('file_task3.txt', "r", encoding='utf-8') as in_f:
    workers = {}
    employees = 0
    sum_pay = 0
    for line in in_f:
        employees += 1
        el, value = line.split()
        workers[el] = value
        sum_pay = sum_pay + int(value)
        if int(value) < 20000:
            print(el, "- зарплата меньше 20 т.р.")
mean = sum_pay / employees
print("\nСредняя зарплата =", mean)