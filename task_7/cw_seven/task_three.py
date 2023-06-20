# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
from pathlib import Path
from typing import TextIO


def new(numbers: Path, words: Path, result: Path) -> None:
    with (
        open(numbers, 'r', encoding='utf-8') as f_num,
        open(words, 'r', encoding='utf-8') as f_words,
        open(result, 'w', encoding='utf-8') as f_res
    ):
        len_numbers = sum(1 for _ in f_num)
        print(type(f_num))
        len_words = sum(1 for _ in f_words)
        for _ in range(max(len_numbers, len_words)):
            num = read_or_begin(f_num)
            words = read_or_begin(f_words)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{words.lower()}, {abs(mult)}\n')
            elif mult >= 0:
                f_res.write(f'{words.upper()}, {round(mult)}\n')


def read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return read_or_begin(fd)
    return line[:-1]

