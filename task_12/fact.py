# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# # их факториалов.
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json


class Factorial:
    _context_dict = dict()

    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
        if len(self.save_list) <= self.k -1:
            self.save_list.append(res)
        else:
            self.save_list.pop(0)
            self.save_list.append(res)
        return self.save_list

    def __enter__(self):
        return self

    def mapper(self):
        for i, value in enumerate(self.save_list, start=1):
            self._context_dict[i] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mapper()
        with open("result_fact", 'w', encoding='utf-8') as f:
            json.dump(self._context_dict, f, indent=2)

    def __str__(self):
        return f'Полученный список: {self.save_list}'


if __name__ == '__main__':
    with Factorial(5) as fact:
        print(fact(5))
        print(fact(6))
        print(fact(6))
        print(fact(6))
        fact(6)
        fact(5)
        print(fact)











