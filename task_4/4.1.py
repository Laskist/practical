# Напишите функцию для транспонирования матрицы

import np as np
import random


def creat_matrix():
    print('Введите количество строк в матрице: ')
    x = int(input())
    print('Введите количество столбцов в матрице: ')
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0, 100))
    return array


matrix = creat_matrix()


def transpose_matrix():
    trans_matrix = []
    for i in range(0, len(matrix[0])):
        trans_matrix.append([])
        for j in range(0, len(matrix)):
            trans_matrix[i].append((matrix[j][i]))
    return trans_matrix


print(matrix)
print(transpose_matrix())

# Проверка транспонировая матрицы

result = np.transpose(matrix)
print(result)
