import pytest
from data import final_check_year


def test_leap_year():
    assert final_check_year("12.12.2000") == 'Високосный'


def test_not_leap_year():
    assert final_check_year("12.12.1993") == 'не является високосным'


def test_year_is_int():
    assert final_check_year(123) == 'Дата заполнена не корректно'


def test_year_is_other_str():
    assert final_check_year("adadsda") == 'Дата заполнена не корректно'


def test_year_bottom_line():
    assert final_check_year("12.12.0000") == 'Дата заполнена не корректно'


def test_year_top_line():
    assert final_check_year("12.12.10000") == 'Дата заполнена не корректно'


if __name__ == '__main__':
    pytest.main(['-v'])