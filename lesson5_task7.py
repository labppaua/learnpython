# -*- coding: utf-8 -*-
# Урок 5 задание 7
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.


import json
profit = {}
profit_file = {}
sum_income = 0
average_income = 0
i = 0
with open("file_task7.txt", "r") as in_file:
    for line in in_file:
        name, f_type, income, consumption = line.split()
        profit[name] = int(income) - int(consumption)
        if profit.setdefault(name) >= 0:
            sum_income = sum_income + profit.setdefault(name)
            i += 1
    if i != 0:
        average_income = sum_income / i
    print("Прибыль средняя =" ,average_income)
    profit_file = {"srednyaya pribyl'": average_income}
# транслитерация так как не разобрался с выводом юникода в файл, нехватило времени вникуть
    profit.update(profit_file)
    print("Итоговый вывод по прибыли:")
    print(profit)

with open("out_file_task7.json", "w") as out_file:
    json.dump(profit, out_file)
    out_prn = json.dumps(profit)
    print("Читаем созданный файл: ")
    print(out_prn)