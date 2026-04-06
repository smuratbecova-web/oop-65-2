class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"I am {self.name}, level {self.level}")

    def attack(self):
        print(f"{self.name} attacks!")

    def rest(self):
        self.health += 1
        print(f"{self.name} rests")



class Vampire(Hero):
    def __init__(self, name, level, health, strength, blood):
        super().__init__(name, level, health, strength)
        self.blood = blood

    def attack(self):
        print(f"{self.name} bites!")


class Werewolf(Hero):
    def __init__(self, name, level, health, strength, rage):
        super().__init__(name, level, health, strength)
        self.rage = rage

    def attack(self):
        print(f"{self.name} attacks with claws!")

import random

vampire = Vampire("Dracula", 5, 10, 7, 5)
werewolf = Werewolf("Lupin", 5, 9, 8, 6)


choice = input("Choose: Vampire / Werewolf\n").lower()

player = vampire if choice == "vampire" else werewolf
enemy = random.choice([vampire, werewolf])

print(f"You chose: {player.__class__.__name__}")
print(f"Enemy: {enemy.__class__.__name__}")


if type(player) == type(enemy):
    print("Draw!")
elif isinstance(player, Vampire):
    print("Vampire wins!")
else:
    print("Werewolf wins!")