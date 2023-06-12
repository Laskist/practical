# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def road(a: str) -> tuple:
    *path, syffix = a.split('/')
    name, extension = syffix.split('.')
    return ('/'.join(map(str, path))), name, extension


print(f'{road("/Users/Mokonajen/Desktop/Собор/IMG_2748.JPG")}')
print(f'{type(road("/Users/Mokonajen/Desktop/Собор/IMG_2748.JPG"))}')

