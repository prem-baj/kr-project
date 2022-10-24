from models import Character

p1 = Character(name="John", hp=100, strength=15, defence=5)
p2 = Character("Mike", hp=100, strength=10, defence=3)


p1.attack(p2)
print(p2.hp)




      