# Урок 7 задание 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, m=[[]]):
        self.matrix = m

    def __str__(self):
        s = ""
        for row in self.matrix:
            s += "|\t"
            for i in row:
                s += "{}\t".format(i)
            s += "|\n"
        return s

    def __add__(self, m=[[]]):
        if len(self.matrix) != len(m):
            return
        for row_matrix, row_m in zip(self.matrix, m):
            if len(row_matrix) != len(row_m):
                return
        for row_matrix, row_m in zip(self.matrix, m):
            l = []
            for el1, el2 in zip(row_matrix, row_m):
                l.append(el1 + el2)
            row_matrix.clear()
            row_matrix.extend(l)



if __name__ == '__main__':
    matrix = Matrix([[8, 14, -6], [12, 7, 4], [-11, 3, 21]])
    print(matrix)
    matrix + [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]
    print(matrix)