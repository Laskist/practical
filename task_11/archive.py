# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Create list-Archive for int and str"""
    numbers = []
    values = []

    def __init__(self, num: int, value: str):
        self.num = num
        self.value = value

    def __new__(cls, num: int, value: str):
        instance = super().__new__(cls)
        cls.numbers.append(num)
        cls.values.append(value)
        return instance


if __name__ == '__main__':
    a = Archive(42, "ghbdtn")
    b = Archive(43, "Hi")
    print(a.numbers)
    print(b.numbers)
    print(b.values)
    c = Archive(44, "Alloha")
    print(f'{c.numbers = }, {c.values = }')
    help(Archive)
