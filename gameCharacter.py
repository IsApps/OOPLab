class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount


character = GameCharacter("Hero", 100)
character.take_damage(30)
character.heal(10)
print(character.health)
