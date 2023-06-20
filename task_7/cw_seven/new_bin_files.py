# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from random import choice, randint


VOWELS = 'aeioyu'
CONCONANTS = 'bcdfghjklmnpqrstvwxz'


def gen_files(extention: str, min_len: int = 6, max_len: int = 30, min_bytes: int = 256,
              max_bytes: int = 4096, num: int = 42):
    for _ in range(num):
        rad_string = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONCONANTS)
                             for i in range(randint(min_len, max_len)))
        date = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(f'{rad_string}.{extention}', 'wb') as f:
            f.write(date)
