# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time


class MySrting(str):
    """expand class str."""
    def __new__(cls, value: str, name: str):
        """expand metod new params value and name"""
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time = time.time()
        return instance

    def __repr__(self):
        return f'MyString {self.name}, {self.time}, {self.value}'

    def __str__(self):
        return f' {self.name}, {self.time}, {self.value}'


if __name__ == '__main__':
    mystr = MySrting("чтото НЕПОНЯТНОЕ", "текст")
    print(mystr.name, mystr.time)
    print(mystr.upper())
    help(MySrting)
    help(mystr)
    print(mystr.__repr__())
    print(mystr)