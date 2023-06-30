# Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
from random import randint

import numpy as np
from numpy import matrix


class Matrix:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def transpose_matrix(self):
        array = []
        for i in range(self.x):
            array.append([])
            for j in range(self.y):
                array[i].append(randint(0, 100))
        print(array)

        trans_matrix = []
        for i in range(0, len(array[0])):
            trans_matrix.append([])
            for j in range(0, len(array)):
                trans_matrix[i].append((array[j][i]))
        return trans_matrix


a = Matrix(3, 4)
print(f'{a.transpose_matrix()}')


