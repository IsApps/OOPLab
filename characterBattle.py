class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character):
        other_character.health -= self.attack_power
        if other_character.health < 0:
            other_character.health = 0

    def is_alive(self):
        return self.health > 0


c1 = Character("Hero", 100, 20)
c2 = Character("Enemy", 80, 15)

while c1.is_alive() and c2.is_alive():
    c1.attack(c2)
    c2.attack(c1)

print(c1.health)
print(c2.health)
