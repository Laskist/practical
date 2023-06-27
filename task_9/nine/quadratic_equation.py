# Нахождение корней квадратного уравнения <br>
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
import math
from typing import Callable
import json
import csv
import random
from functools import cache
from functools import wraps


def quadratic(func: Callable) -> tuple:
    @wraps(func)
    def wrapper(*args, **kwargs):
        rnd_num = func(*args, **kwargs)
        csv_list = []
        result = {}
        with open(f'{func.__name__}.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                csv_list.append(line)
            for i in range(len(csv_list)):
                a, b, c = list(map(int, csv_list[i]))
                if a == 0:
                    res = f'a = {a}, нахождение дискриминанта невозможно'
                    result[f"{a}, {b}, {c}"] = res
                elif a !=0:
                    discr = b ** 2 - 4 * a * c
                    if discr > 0:
                        x1 = (-b + math.sqrt(discr)) / (2 * a)
                        x2 = (-b - math.sqrt(discr)) / (2 * a)
                        res = (x1, x2)
                        result[f"{a}, {b}, {c}"] = res
                    elif discr == 0:
                        x = -b / (2 * a)
                        res = x
                        result[f"{a}, {b}, {c}"] = res
                    else:
                        res = 'Корней нет'
                        result[f"{a}, {b}, {c}"] = res
        return result
    return wrapper


def json_file(func: Callable):

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=2, ensure_ascii=False)
        return func(*args, **kwargs)
    return wrapper


@json_file
@cache
@quadratic
def create_csv():
    MIN_STR = 100
    MAX_STR = 1000
    MIN_NUM = -1000
    MAX_NUM = 1000
    NUM = 3
    list = random.randrange(MIN_STR, MAX_STR)
    for _ in range(list):
        num = random.sample((range(MIN_NUM,MAX_NUM)), NUM)
        with open('create_csv.csv', 'a', newline='', encoding='utf-8') as f_write:
            w = csv.writer(f_write)
            w.writerow(num)

