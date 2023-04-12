class Pet:
    def __init__(self):
        self.name = None
        self.type = None
        self.age = None
with open("10.01 Pets.txt", "r") as f:
    pets = []
    for line in f:
        name, pet_type, age = line.strip().split(", ")
        pet = Pet()
        pet.name = name
        pet.type = pet_type
        pet.age = int(age)
        pets.append(pet)
for pet in pets:
    print(pet.name, pet.type, pet.age)