# Добавьте методы представления экземпляра для программиста
# и для пользователя в архив.

class Archive:
    """Create list-Archive for int and str"""
    numbers = []
    values = []

    def __init__(self, num: int, value: str):
        """storing variables"""
        self.num = num
        self.value = value

    def __new__(cls, num: int, value: str):
        instance = super().__new__(cls)
        cls.numbers.append(num)
        cls.values.append(value)
        return instance

    def __str__(self):
        return f'Добавлен номер: {self.num}, строка: {self.value}. Итоговый список чисел {self.numbers}, список строк {self.values}'

    def __repr__(self):
        return f'Archive {self.numbers}, {self.values}'


if __name__ == '__main__':
    a = Archive(42, "ghbdtn")
    b = Archive(43, "Hi")
    print(a.numbers)
    print(b.numbers)
    c = Archive(44, "Alloha")
    print(f'{c.numbers = }, {c.values = }')
    print(c.__repr__())
    print(f'{c = }')
    print(c)
    help(Archive)