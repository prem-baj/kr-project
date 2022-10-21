class Character:
    def __init__(self, name, hp=100.0, strength=0.0, defence=1.0):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence

    def attack(self, opponent):
        damage = self.strength - opponent.defence
        if damage < 1:
            damage = 1
        opponent.hp = opponent.hp - damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage")


