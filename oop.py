# create classes that organises functions together
# organise classes into modules
# object is an instance of a class (blueprint)

class Person:
    number_of_people = 0 # class attribute and does not have access to the instance of a class

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod # refers to only accessing the class attributes (no access to self)
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

    @staticmethod
    def add5(x):
        return x+5
p1 = Person('Tim')
p2 = Person('Bon')

print(Person.number_of_people)
print(Person.add5(5))