# Урок 4 задание 2
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [el for pos, el in enumerate(my_list) if pos > 0 and el > my_list[pos-1] ]
print(new_list)