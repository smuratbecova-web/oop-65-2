from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} is ready for battle!"


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Mage {self.name} opens a portal! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Warrior {self.name} throws his shield! Level: {self.lvl}"


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name}, Balance: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Balance: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return "Error: Cannot add accounts of different hero classes!"

    def __eq__(self, other):
        return (
            type(self.hero) == type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Code: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text" "Code":"1234","phone": phone}



mage1 = MageHero("Doctor Strange", 60, 1000, 300)
mage2 = MageHero("Doctor Strange", 60, 1000, 400)
warrior = WarriorHero("Captain America", 40, 2000, 100)

acc1 = BankAccount(mage1, 10000, "1234", "Simba")
acc2 = BankAccount(mage2, 7000, "0202", "Simba")
acc3 = BankAccount(warrior, 15000, "8787", "Simba")

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)

print("Bank:", acc1.get_bank_name())
print("Level bonus:", acc1.bonus_for_level(), "SOM")

print("\n=== __add__ check ===")
print("Sum of two mages:", acc1 + acc2)
print("Mage + Warrior:", acc1 + acc3)

print("\n=== __eq__ check ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp("+996777123456"))