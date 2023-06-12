# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def gen(n) -> str:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(f'{list(gen(12))}')
