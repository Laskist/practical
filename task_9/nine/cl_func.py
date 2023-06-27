# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов
import random
from typing import Callable


def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count < MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
            print(input_count)
        if MIN_NUM > input_num < MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper


@deco
def closure(count: int, num: int) -> Callable[[], None]:
    def rnd_num():
        for i in range(1, count + 1):
            user_input = int(input('Введите число для отгадывания: '))
            if user_input < num:
                print('Загаданное число больше')
            elif user_input > num:
                print('Загаданное число меньше')
            else:
                print(f'Вы угадали c {i} попытки!')
                break
        else:
            print(f'Вы не угадали')

    return rnd_num


if __name__ == '__main__':
    res = closure(0, 20)
    res()


