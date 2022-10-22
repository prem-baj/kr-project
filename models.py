class Character:
    def __init__(self, name, hp=100.0, strength=0.0, defence=1.0):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence

    def attack_strenght(self,strength):
        import random
        self.strength = strength
        probability = [0.7,0.8,0.9,1,1.1,1.2,1.3]
        random_num = random.choice(probability)
        final_damage = self.strength *random_num
        return f'Your attack damage is {final_damage}'

    def attack(self, opponent):
        damage = self.final_damage - opponent.defence
        if damage < 1:
            damage = 1
        opponent.hp = opponent.hp - damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage")


