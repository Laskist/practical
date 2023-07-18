import logging
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='triangle.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)

def triangle(a: float, b: float, c: float):
    if a == 0 or b == 0 or c == 0:
        logger.error(f'Треугольник со сторонами {a}, {b} и {c} не существует, т.к. одна из сторон = 0')
        return f'сторона не может быть равной нулю'
    elif a < 0 or b < 0 or c < 0:
        logger.error(f'Треугольник со сторонами {a}, {b} и {c} не существует, т.к. одна из сторон < 0')
        return f'сторона не может быть отрицательной'
    elif (a >= b + c) or (b >= a + c) or (c >= b + a):
        logger.error(f'Треугольник со сторонами {a}, {b} и {c} не существует, т.к. сумма двух сторон больше длины третьей')
        return f'Треугольника с такими сторонами не существует'
    elif a == b and a == c:
        result = f'Треугольник равносторонний'
        logger.info(f'{a}, {b}, {c} = {result}')
        return result
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        result = f'Треугольник равнобедренный'
        logger.info(f'{a}, {b}, {c} = {result}')
        return result
    else:
        result = f'Треугольник разносторонний'
        logger.info(f'{a}, {b}, {c} = {result}')
        return result

    # logger.info(f'{a}, {b}, {c} = {result}')


if __name__ == '__main__':
    # print(triangle(3, 4, 3))
    parser = argparse.ArgumentParser(description='Вводим стороны треугольника')
    parser.add_argument('-a', metavar='a', type=float)
    parser.add_argument('-b', metavar='b', type=float)
    parser.add_argument('-c', metavar='c', type=float)
    args = parser.parse_args()
    print(triangle(args.a, args.b, args.c))

