class Character:
    def __init__(self, name, hp=100.0, strength=0.0):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, opponent):
        opponent.hp = opponent.hp - self.strength
        print(f"{self.name} attacks {opponent.name} and deals {self.strength} damage")

