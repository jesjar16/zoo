class Animal:
    def __init__(self, name, age, health_level, happiness):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness = happiness

    def feed(self, klgs):
        self.health_level = self.health_level + 10 * klgs
        self.happiness = self.happiness + 10 * klgs

    def display_info(self):
        return f"Nombre: {self.name}, Edad: {self.age} , Salud: {self.health_level}, Felicidad: {self.happiness}"
    
class Lion(Animal):
    def __init__(self, name, age, color, health_level=80, happiness=50):
        super().__init__(name, age, health_level, happiness)
        self.color = color	
    def display_info(self):
        return f"Nombre: {self.name}, Edad: {self.age} , Salud: {self.health_level}, Felicidad: {self.happiness}, Color: {self.color}"

class Tiger(Animal):
    def __init__(self, name, age, health_level=60, happiness=70):
        super().__init__(name, age, health_level, happiness)	

class Bear(Animal):
    def __init__(self, name, age, health_level=40, happiness=80):
        super().__init__(name, age, health_level, happiness)	

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, animal_type, name, age, *color):
        self.animals.append(animal_type(name, age, *color))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print (animal.display_info())

# Creamos directamente a través de las subclases de animales
print ("*"*50 + " Creando animales directamente... " + "*"*50)

# Se crea objeto Lion
lion1 = Lion('Simba', 5, "amarillo")

# Se imprime información actual del animal
print (lion1.display_info())

# Se crea objeto Tiger
tiger1 = Tiger('Tony', 7)

# Se imprime información actual del animal
print (tiger1.display_info())

# Se crea objeto Bear
bear1 = Bear('Yogui', 10)

# Se imprime información actual del animal
print (bear1.display_info())

print ("*"*50 + " Se alimenta a los animales... " + "*"*50)

# Se alimenta a Lion
lion1.feed(15)

# Se imprime información actual del animal
print (lion1.display_info())

# Se alimenta a Tiger
tiger1.feed(15)

# Se imprime información actual del animal
print (tiger1.display_info())

# Se alimenta a Bear
bear1.feed(15)

# Se imprime información actual del animal
print (bear1.display_info())

# Se crea Zoológico
print ("*"*50 + " Creando zoologico... " + "*"*50)
zoo1 = Zoo("Jessica's Zoo")

# Se agrega Tiger al zoológico
print ("*"*50 + " Agregando animales al zoologico... " + "*"*50)
zoo1.add_animal(Tiger, "Tigrecito", 2)
zoo1.add_animal(Bear, "Winnie", 6)
zoo1.add_animal(Lion, "Mufasa", 12, "cafe")

# Mostrar todos los animales
print ("*"*50 + " Mostrando animales del zoologico... " + "*"*50)
zoo1.print_all_info()