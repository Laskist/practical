# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json


def add_data(name: str, personal_id: int, level: int) -> dict[int, dict[str, int]]:
    return {level: {personal_id: name}}


def write_json(data: dict) -> None:
    file = '../json.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def ui():
    exit_program = False
    print("Добро пожаловать! Введите данные для создания файла: ")
    while not exit_program:
        personal_id = int(input('Введите id: '))
        name = input('Введите имя: ')
        level = int(input('Введите уровень доступа: '))
        continue_program = input('Хотите продолжить? Да/нет: ')
        if continue_program == 'нет':
            exit_program = True
        write_json(add_data(name, personal_id, level))

