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
        instance.name = name
        instance.time = time.time()
        return instance

if __name__ == '__main__':
    mystr = MySrting("чтото НЕПОНЯТНОЕ", "текст")
    print(mystr.name, mystr.time)
    print(mystr.upper())
    help(MySrting)
    help(mystr)