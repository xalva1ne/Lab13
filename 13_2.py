
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)


classes = []

for i in range(10):
    className = f'Class{i}'
    newClass = Meta(className, (), {})
    classes.append(newClass)
    print(newClass.__name__)

print(classes)
