# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animals:

    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        return

    def say(self):
        return

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.age}'


class Birds(Animals):

    def __init__(self, name, weight, age, bird_type, sound):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.bird_type}, {self.move()}, {self._sound}'


class Fish(Animals):
    def __init__(self, name, weight, age, fish_type):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Swim"

    def say(self):
        return "Молчалив"

    def __str__(self):
        return f'{super().__str__()} {self.fish_type}, {self.move()}, {self.say()}'


class Dogs(Animals):
    def __init__(self, name, weight, age, dog_type):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "Run"

    def say(self):
        return "Goy"

    def __str__(self):
        return f'{super().__str__()} {self.dog_type}, {self.move()}, {self.say()}'


if __name__ == '__main__':
    dog = Dogs("Алекс", 25, 4, "Корги")
    bird = Birds("Глаша", "0,3", 8, "Попугай", "Чирикает")
    fish = Fish("Карп", 2, 1, "Карповые")
    print(dog)
    print(bird)
    print(fish)