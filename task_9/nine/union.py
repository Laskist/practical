# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров, декоратором контроля значений и декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from typing import Callable
import json
import random
from functools import cache


def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count  or input_count < MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        if MIN_NUM > input_num < MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper


def count(cnt: int):
    def new_list(func: Callable):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(cnt):
                    result = func(*args, **kwargs)
            return result
        return wrapper
    return new_list


def create_json(func: Callable):
    final_dict = {}

    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        a, b = args
        print(a, b)
        for i in range(len(args)):
            final_dict.update({f'Загаданное число: {b}, Попытки {a}': f'Угадано с: {i}'})
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
            json.dump(final_dict, f, indent=2, ensure_ascii=False)
        return func(*args, **kwargs)
    return wrapper


@deco
@create_json
@count(2)
def closure(my_count: int, n: int) -> Callable[[], None]:
    def rnd_num():
        for i in range(1, my_count + 1):
            user_input = int(input('Введите число для отгадывания: '))
            if user_input < n:
                print('Загаданное число больше')
            elif user_input > n:
                print('Загаданное число меньше')
            else:
                print(f'Вы угадали c {i} попытки!')
                break
        else:
            print(f'Вы не угадали')

    return rnd_num


if __name__ == '__main__':
    res = closure(15, 0)
    res()

# f2.deco(f2.closure(3, 20))
# f3.deco(f3.multy(4, 2, c=3, d=7))
# f4.deco(f4.fact(3))
