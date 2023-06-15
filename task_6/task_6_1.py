# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from datetime import datetime


def _check_year2(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 400
    CHECK_NORMAL_3 = 100
    YEAR_START = 1
    YEAR_END = 9999
    year = int(date.split(".")[-1])

    if YEAR_START<year<YEAR_END and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 ==0:
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

    :rtype: object
    """
    if check_year(date):
        return 'Високосный' if _check_year2(date) else "не является високосным"
    else:
        return f"Дата заполнена не корректно"


