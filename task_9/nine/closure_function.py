# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from typing import Callable


def closure(count: int, n: int) -> Callable[[], None]:
    def rnd_num():
        for i in range(1, count + 1):
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


res = closure(5, 20)
res()
