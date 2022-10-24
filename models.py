from typing import DefaultDict


class Character:
    def __init__(self, name, hp=100.0, strength=0.0, defence=1.0):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence
        
    def attack(self,opponent): 
        damage = self.strength - opponent.defence
        while opponent.hp >= 0:
            if opponent.hp <= 100:
                opponent.hp -= damage
                print ('%s hits %s for %s, %s hp left %s' %(self.name,opponent.name,damage,opponent.name,opponent.hp))
            elif opponent.hp <= 0:
                print ('%s has killed %s' %(self.name,opponent.name))
            if self.hp <= 0:
                print ("%s is dead" %(self.name))
                   