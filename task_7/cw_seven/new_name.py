# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice, randint
from pathlib import Path

VOWELS = 'aeioyu'
CONCONANTS = 'bcdfghjklmnpqrstvwxz'


def fail_name(count: int, file: str| Path, str_min: int = 4, str_max: int = 7) -> None:
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONCONANTS)
                           for i in range(randint(str_min,str_max)))
            f.write(f'{name.capitalize()}\n')
