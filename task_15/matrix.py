import logging
from pprint import pprint
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='func.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class Matrix:
    """matrix operation: sum, subtraction, multiplication"""

    def __new__(cls, matrix_1, matrix_2):
        """saving variable matrices"""
        instance = super().__new__(cls)
        instance.matrix_1 = matrix_1
        instance.matrix_2 = matrix_2
        return instance

    def comparison(self):
        if len(self.matrix_1) == len(self.matrix_2):
            for i in range(0, len(self.matrix_1)):
                if len(self.matrix_1[i]) == len(self.matrix_2[i]):
                    for j in range(len(self.matrix_2[i])):
                        if self.matrix_1[i][j] == self.matrix_2[i][j]:
                            None
                        else:
                            logger.error(f'Матрицы {self.matrix_1} and {self.matrix_2} не равны')
                            return f'Матрицы не равны'
            return f'Матрицы равны'
        else:
            logger.error(f'{self.matrix_1} and {self.matrix_2} не равны')
            return f'Матрицы не равны'

    def sum_matrix(self):
        """addition of matrices with checking one to the same size"""
        sum_mtrx = []
        if len(self.matrix_1) == len(self.matrix_2):
            for i in range(0, len(self.matrix_1)):
                if len(self.matrix_1[i]) == len(self.matrix_2[i]):
                    sum_mtrx.append([])
                    for j in range(0, len(self.matrix_1[0])):
                        res = self.matrix_1[i][j] + self.matrix_2[i][j]
                        sum_mtrx[i].append(res)
                else:
                    logger.error(
                        f'Матрицы {self.matrix_1} and {self.matrix_2} нельзя складывать, т.к. они разного размера')
                    return f'Складывать матрицы разного размера нельзя'
            return sum_mtrx
        else:
            logger.error(f'Матрицы {self.matrix_1} and {self.matrix_2} нельзя складывать, т.к. они разного размера')
            return f'Складывать матрицы разного размера нельзя'

    #
    def subtracting_matrix(self):
        """subtraction of matrices with checking for the same size"""
        sub_mtrx = []
        if len(self.matrix_1) == len(self.matrix_2):
            for i in range(0, len(self.matrix_1)):
                if len(self.matrix_1[i]) == len(self.matrix_2[i]):
                    sub_mtrx.append([])
                    for j in range(0, len(self.matrix_1[i])):
                        res = self.matrix_1[i][j] - self.matrix_2[i][j]
                        sub_mtrx[i].append(res)
                else:
                    logger.error(f'{self.matrix_1} and {self.matrix_2} нельзя вычитать, т.к. они разного размера')
                    return f'Вычитать матрицы разного размера нельзя'
            return sub_mtrx
        else:
            logger.error(f'Матрицы {self.matrix_1} and {self.matrix_2} нельзя вычитать, т.к. они разного размера')
            return f'Вычитать матрицы разного размера нельзя'

    #
    def mult_matrix(self):
        """calculation of the multiplication of matrices with a check for dimension"""
        mult_mtrx = [[0 for _ in range(len(self.matrix_2[0]))] for _ in range(len(self.matrix_1))]
        for i in range(len(self.matrix_1)):
            if len(self.matrix_1[i]) == len(self.matrix_2):
                for j in range(len(self.matrix_2[0])):
                    for k in range(len(self.matrix_2)):
                        mult_mtrx[i][j] += self.matrix_1[i][k] * self.matrix_2[k][j]
            else:
                return f'Перемножать матрицы разной размерности нельзя'
        return mult_mtrx
    #
    def __str__(self):
        logger.info(f'{self.matrix_1}, {self.matrix_2} = сумма = {self.sum_matrix()}, '
                    f'вычитание = {self.subtracting_matrix()}. Умножение : {self.mult_matrix()}')
        return f' Матрица 1: {self.matrix_1}, матрица 2 :{self.matrix_2}, сумма = {self.sum_matrix()},' \
               f' вычитание = {self.subtracting_matrix()}. Умножение : {self.mult_matrix()}'


if __name__ == '__main__':
    # mtrx_1 = Matrix([[1, 2, 6], [3, 4, 5]], [[1, 3, 5], [3, 5, 7]])
    # print(mtrx_1.comparison())
    # pprint(mtrx_1.sum_matrix(), width=20)
    # pprint(mtrx_1.subtracting_matrix(), width=20)
    # print(mtrx_1)
    # print(mtrx_1.mult_matrix()) #разная размерность, перемножать нельзя
    # mtrx_1 = Matrix([[1, 2, 6], [3, 4, 5]], [[1, 3, 5], [3, 5, 7], [3, 5, 8]])
    # print(mtrx_1.mult_matrix())
    # print(mtrx_1.sum_matrix(), mtrx_1.subtracting_matrix()) #разный размер, сложение и вычитание невозможно
    # mtrx_2 = Matrix([[4, 5], [6, 7]], [[1, 3], [8, 11]])
    # mtrx_2 = Matrix([[4, 5], [6, 7]], [[1, 3], [8, 11], [11, 15]])  #разная размерность, перемножать нельзя
    # print(mtrx_2.mult_matrix())
    # mtrx_3 = Matrix([[4, 5, 0, 0, 0], [6, 7, 0, 0, 0], [0, 0, 0, 0, 0]], [[1, 3, 0], [8, 11, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # print(mtrx_3.mult_matrix())
    parser = argparse.ArgumentParser(description='Получаем две матрицы')
    parser.add_argument('-matrix_1', nargs='*')
    parser.add_argument('-matrix_2', nargs='*')
    args = parser.parse_args()
    print(Matrix(args.matrix_1, args.matrix_2))
    # -matrix_1[[4, 5], [6, 7]] - matrix_2[[1, 3], [8, 11]]

    # print(mtrx_1)
