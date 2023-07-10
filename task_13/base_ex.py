# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class CustomException(Exception):
    pass


class LvlError(Exception):
    pass


class AccessError(Exception):
    pass


class ConditionError(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f'Вы ввели некорректное число {self.n}. \n Попробуйте еще раз'


class LengthError(Exception):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def __str__(self):
        return f'Ни одна из сторон прямоугольника не может быть меньше 0. Вы ввели стороны {self.l}, {self.w}'


