# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
from typing import Callable


def deco(func: Callable):
    final_dict = {}
    # with open(f'{func.__name__}.json', 'r') as f:
    #     final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # for i in range(len(args)):
        final_dict.update({str(res): args})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)
        # return func(*args, **kwargs)
    return wrapper


@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a*b

multy(4, 2, c=3, d=7)

