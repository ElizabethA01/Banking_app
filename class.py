# class is the blueprint which has attributes (properties) and methods (actions)
# you can create instances a.k.a objects by instantiating a class 
# OOP allows code to be repeatable, well organised and memory efficient
# similar to a datatype / object such as str or list which have methods


class PlayerCharacter:
    # Class Object Attribute
    membership = True # static attribute that can't be modified 
    # defined in constructor method
    def __init__(self, name='Anonymous', age = 9) -> None:
        # if (PlayerCharacter.membership): # membership can be accessed with class name because it's a class object attribute
        if age > 18: 
            self.name = name # self refers to the actual object for instance player1 or player2
            self.age = age # dynamics attributes (self makes it dynamic)
    
    def run(self):
        print('run')
    
    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Charlie', 55) # instantiating a class to create an instance 
print(player1.membership)
player1.run()
player1.shout()


# help(list) shows you the blueprint of an object


class Cat:
    species = 'mammal'
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

# create instances 
cat1 = Cat('Bob', 4)
cat2 = Cat('Jill', 5)
cat3 = Cat(name='Sue', age=10)
#create a function to find oldest cat
def find_oldest(*cats):
    age = 0
    oldest = {}
    for cat in cats:
        if cat.age > age:
            age = cat.age
            oldest = {'name': cat.name, 'age': cat.age}
    return oldest

cat = find_oldest(cat1, cat2, cat3)
print(f'{cat["name"]} is {cat["age"]} years old.')


class Person:
    age: int = 20
    race: str = 'caucasian'

    def __init__(self, age, race) -> None:
        self.age = age
        self.race = race

class Female(Person):
    cup_size: int = 32
    
    def __init__(self, age, race) -> None:
        super().__init__(age, race)
    

Stacy = Female()
print(Stacy.cup_size)
print(Stacy.age)

# dynamic classes are classes to define characters/ objects and architectural classes are used to define functions 
class Pets:
    animals = []
    def __init__(self, animals) -> None:
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
    
    def sing(self):
        for animal in self.animals:
            print(animal.sing())

class Cat:
    is_lazy = True 

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def walk(self):
        return f'{self.name} is walking around!'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def __init__(self, sounds, name, age) -> None:
        super().__init__(name, age)
        self.sounds = sounds
        
    def sing(self, sounds):
        return f'{sounds}'

# add another cat
class Bob(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 3), Sally(sounds = 'NOO', name='Sally', age = 3), Bob('Bob', 3)]

#Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# Output all of the cats walking using the my_pets instance
my_pets.walk()
# my_pets.sing()