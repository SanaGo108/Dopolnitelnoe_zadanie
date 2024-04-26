import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест.")

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} гав")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} мяу")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} мууу")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} поет.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает звук.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_zoo(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            print("Zoo saved to", filename)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

zoo = Zoo()
zoo.add_animal(Dog("Дружок", 3))
zoo.add_animal(Cat("Мурка", 2))
zoo.add_animal(Cow("Зорька", 5))

keeper = ZooKeeper("Петя")
vet = Veterinarian("Маша")

zoo.add_staff(keeper)
zoo.add_staff(vet)

keeper.feed_animal(zoo.animals[0])  # Feeding the first animal
vet.heal_animal(zoo.animals[1])    # Healing the second animal

zoo.save_zoo('zoo.pkl')

loaded_zoo = Zoo.load_zoo('zoo.pkl')
print("Loaded zoo has", len(loaded_zoo.animals), "animals.")
animal_sound(loaded_zoo.animals)
