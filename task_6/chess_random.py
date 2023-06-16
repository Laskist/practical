# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
from random import shuffle
from typing import Tuple


def func_random(x: list, y: list, try_count: int) -> tuple[list, list]:
    num = 8
    count = 1
    print(x, y)
    while count <= try_count:
        print(count)
        for i in range(num):
            for j in range(i + 1, num):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    break
            else:
                count += 1
                print(count)
                print(x, y)
                shuffle(y)

    return None
