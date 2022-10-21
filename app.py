from models import Character

p1 = Character(name="John", hp=100, strength=15)
p2 = Character("Mike", hp=100, strength=10)

p1.attack(p2)
print(p2.hp)