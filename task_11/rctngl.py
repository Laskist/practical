# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, l, w = None):
        self.l = l
        self.w = w
        if w is None:
            self.w = l

    def perimeter(self):
        return 2 * (self.l + self.w)

    def area(self):
        return self.l * self.w

    def __add__(self, other):
        """Взяла одну сторону как сумму периметров, вторую как разницу"""
        c = self.perimeter() + other.perimeter()
        if self.perimeter() - other.perimeter() > 0:
            d = self.perimeter() - other.perimeter()
        else:
            d = other.perimeter() - self.perimeter()
        return Rectangle(c, d)


if __name__ == '__main__':
    rect_1 = Rectangle(3, 3)
    print(f'{rect_1.perimeter() = }, {rect_1.area() = }')
    rect_2 = Rectangle(4, 4)
    print(f'{rect_2.perimeter() = }, {rect_2.area() = }')
    rect = rect_1 + rect_2
    print(f'{rect.perimeter() = }, {rect.area() = }')
    help(Rectangle)

