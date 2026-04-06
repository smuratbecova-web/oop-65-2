class Vampire:
    def __init__(self, name, health, level, strength):
        self.name = name
        self.health = health
        self.level = level
        self.strength = strength

    def greet(self):
        return f"I am vampire {self.name}, level {self.level}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} bites!"

    def rest(self):
        self.health += 1
        return f"{self.name} rests"


class Werewolf:
    def __init__(self, name, health, level, strength):
        self.name = name
        self.health = health
        self.level = level
        self.strength = strength

    def greet(self):
        return f"I am werewolf {self.name}, level {self.level}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} attacks!"

    def rest(self):
        self.health += 1
        return f"{self.name} rests"


vamp = Vampire("Dracula", 10, 5, 7)
wolf = Werewolf("Lupin", 8, 4, 6)

print(vamp.greet())
print(vamp.attack())
print(vamp.rest())

print(wolf.greet())
print(wolf.attack())
print(wolf.rest())