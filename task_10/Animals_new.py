# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from animals import Dogs, Fish, Birds


class Factory(object):
    def make_animal(self, animal_type, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    @staticmethod
    def _get_maker(animal_type):
        types = {"dog": Dogs, "bird": Birds, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    factory = Factory()
    animal_factory = factory.make_animal('dog', "Бэмби", 25, 5, "Бультерьер")


    print(animal_factory)
    print(factory.make_animal('fish', "Сом", 5, 3, "Речной"))
    print(factory.make_animal('Bird', "Ель", 4, 4, "Филин", "Ухает"))