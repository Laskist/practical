# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv
from pathlib import Path
import pprint


class Validate:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.isalpha() or not value.istitle():
            raise ValueError(f'Значение {value} должно быть с заглавной буквы и состоять только из букв')


class Student:
    first_name = Validate()
    last_name = Validate()
    surname = Validate()
    _lessons = None

    def __init__(self, first_name: str, last_name: str, surname: str, lessons: Path):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.lessons = lessons

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, less: Path):
        if self.lessons is not None:
            raise ValueError(f'Предметы уже определены')
        self._lessons = {"предметы": {}}
        with open(less, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self._lessons["предметы"][row[0]] = {"оценка": [],
                                                    "тест": [],
                                                    "среднее за тест": None}
        self._lessons["среднее по оценкам"] = None

    def grade(self, name_of_lesson: str, number: int, type_est: str = "less"):
        if name_of_lesson not in self.lessons['предметы'].keys():
            raise ValueError(f'Предмет не найден')
        if type_est == "less":
            if number < 2 or number > 5:
                raise AttributeError(f'Оценка может быть от 2 до 5')
            self.lessons["предметы"][name_of_lesson]["оценка"].append(number)
            self.lessons["среднее по оценкам"] = self.middle_grade(self.lessons)

    def rating(self, name_of_lesson: str, number: int, type_est: str = "less"):
        if name_of_lesson not in self.lessons['предметы'].keys():
            raise ValueError(f'Предмет не найден')
        if type_est == "less":
            if number < 0 or number > 100:
                raise AttributeError(f'Оценка за тест может быть от 0 до 100')
            self.lessons["предметы"][name_of_lesson]["тест"].append(number)
            self.lessons["предметы"][name_of_lesson]["среднее за тест"] = \
                sum(self.lessons["предметы"][name_of_lesson]["тест"]) / len(
                    self.lessons["предметы"][name_of_lesson]["тест"])

    @staticmethod
    def middle_grade(lessons: dict):
        middle_grade = []
        for name_of_lesson in lessons["предметы"]:
            middle_grade.extend(lessons["предметы"][name_of_lesson]["оценка"])
        return sum(middle_grade)/len(middle_grade)

    def __str__(self):
        return f'Студент: {self.last_name} {self.first_name} {self.surname}, \n' \
               f'{self._lessons} '


if __name__ == '__main__':
    st = Student("Денис", "Иванов", "Вадимович", Path('class.csv'))
    st.grade("математика", 5)
    st.rating("математика", 60)
    st.grade("математика", 4)
    st.rating("математика", 80)
    st.grade("физика", 4)
    st.rating("физика", 90)
    st.rating("физика", 60)
    st.grade("химия", 5)
    st.grade("химия", 5)
    st.rating("химия", 90)
    st.grade("информатика", 3)
    st.rating("информатика", 50)
    st.grade("русский язык", 3)
    st.rating("русский язык", 40)
    st.grade("литература", 2)
    st.rating("литература", 40)
    st.rating("литература", 60)
    print(st)
