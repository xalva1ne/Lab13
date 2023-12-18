class Meta(type):
    def __new__(cls, name, bases, dct):
        def say(self):
            return self.word
        dct['say'] = say
        return super().__new__(cls, name, bases, dct)


class Animal(metaclass=Meta):
    def __init__(self, word):
        self.word = word


Dog = Animal('Woof!')
Cat = Animal('Meow!')
print(Dog.say())
print(Cat.say())

# Метод __new__ вызывается при создании нового класса
# cls - метакласс, name - имя класса, bases - кортеж базовых классов,
# dct - словарь с атрибутами класса
