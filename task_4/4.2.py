# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def function_keys(**kwargs) -> object:
    dict_function = dict(zip(kwargs.values(), kwargs.keys()))
    return dict_function


print(function_keys(low=4, cat='hi', dog='привет'))


