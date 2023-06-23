# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
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


def create_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f_2:
        json.dump(file_data, f_2, ensure_ascii=False, indent=2)
