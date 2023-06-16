# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
from random import shuffle
from typing import Tuple


def func_random(x: list, y: list, try_count: int) -> bool:
    num = 8
    count = 1
    while count <= try_count:
        result = True
        for i in range(num):
            for j in range(i + 1, num):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    result = False
        if result:
            count += 1
            print(count)
            print(x, y)
            shuffle(y)
        else:
            shuffle(y)
    return


# print(func_random(x=[int(i + 1) for i in range(8)], y=[1, 2, 3, 4, 5, 6, 7, 8], try_count=4))
