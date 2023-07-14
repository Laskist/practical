import pytest
from matrix import Matrix


def test_not_equality():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5]], matrix_2=[[1, 3, 5],
                                                    [3, 5, 7]]).comparison() == 'Матрицы не равны'


def test_equality():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5]],
                                    matrix_2=[[1, 2, 6], [3, 4, 5]]).comparison() == 'Матрицы равны'


def test_sum_matrix():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5]],
                                    matrix_2=[[1, 3, 5], [3, 5, 7]]).sum_matrix() == [[2, 5, 11], [6, 9, 12]]


def test_sum_matrix_error():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5], [1, 2, 6]],
                        matrix_2=[[1, 2, 6], [3, 4, 5]]).sum_matrix() =='Складывать матрицы разного размера нельзя'


def test_subtracting_matrix():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5]],
                                    matrix_2=[[1, 3, 5], [3, 5, 7]]).subtracting_matrix() == [[0, -1, 1], [0, -1, -2]]


def test_subtracting_matrix_error():
    assert Matrix.__new__(cls=Matrix, matrix_1=[[1, 2, 6], [3, 4, 5], [1, 2, 6]],
                matrix_2=[[1, 2, 6], [3, 4, 5]]).subtracting_matrix() == 'Вычитать матрицы разного размера нельзя'


if __name__ == '__main__':
    pytest.main(['-v'])