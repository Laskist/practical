import doctest
from datetime import datetime


def _check_year2(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEAR_START = 1
    YEAR_END = 9999
    year = int(date.split(".")[-1])
    if YEAR_START < year < YEAR_END and (year % CHECK_NORMAL_1 == 0) and (year % CHECK_NORMAL_2 != 0) or (year % CHECK_NORMAL_3 == 0):
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def final_check_year(date: str) -> str:
    """
    Функция получается строковое представлление даты dd.mm.yyyy и возвращает, каким является год.
    На ввод принимаются года от 0001 до 9999
    >>> final_check_year("12.12.2000")
    'Високосный'
    >>> final_check_year("12.12.1993")
    'не является високосным'
    >>> final_check_year(123)
    'Дата заполнена не корректно'
    >>> final_check_year("adadsda")
    'Дата заполнена не корректно'
    >>> final_check_year("12.12.0000")
    'Дата заполнена не корректно'
    >>> final_check_year("12.12.10000")
    'Дата заполнена не корректно'
    """
    if check_year(date):
        return 'Високосный' if _check_year2(date) else "не является високосным"
    else:
        return f"Дата заполнена не корректно"


if __name__ == '__main__':
    f = final_check_year("12.12.1992")
    print(f)
    doctest.testmod(verbose=True)