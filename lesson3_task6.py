# Урок 3 задание 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def wd_ch_up(s):
    """переводит первый символ слова либо строки в верхний регистр, можно использовать .title() либо .capitalize() но функция не для легких путей"""
    a = s[0].upper()
    b = s[1:]
    return a + b

list_a = input("Введите список слов через пробел для получения чудо-реультата ")
list_a = list_a.split()
f = len(list_a)
i = 0
list_b = ""
while i < f:
    word = list_a[i]
    word = wd_ch_up(word)
    list_b = str(list_b) + word + " "
    i = i + 1
list_b = list_b[:-1]
print(list_b)