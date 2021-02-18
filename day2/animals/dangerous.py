from animals import Animal

class Mammals(Animal):
    def __init__(self):
        self.name = "Mammals"
        self.members = ["Tiger", "Elephant", "Wild Cat"]

class Fish(Animal):
    def __init__(self):
        self.name = "Fish"
        self.members = ["Piranha", "Pufferfish", "Barracuda"]