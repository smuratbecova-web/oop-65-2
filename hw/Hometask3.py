from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Hello, I am {self.name}, level {self.level}")

    def rest(self):
        print(f"{self.name} rests")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass



class Warrior(Hero):
    def attack(self):
        print(f"{self.name} attacks with hammer!")


class Mage(Hero):
    def attack(self):
        print(f"{self.name} uses magic!")


class Assassin(Hero):
    def attack(self):
        print(f"{self.name} attacks silently!")



warrior = Warrior("Thor", 10, 15, 10)
mage = Mage("Doctor Strange", 12, 12, 9)
assassin = Assassin("Black Widow", 9, 10, 8)


warrior.greet()
warrior.attack()
warrior.rest()

print("-----")

mage.greet()
mage.attack()
mage.rest()

print("-----")

assassin.greet()
assassin.attack()
assassin.rest()