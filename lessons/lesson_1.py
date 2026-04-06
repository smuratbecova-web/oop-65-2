# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Hero:
 def __init__(self, name, hp, lvl):
self.name = name
        self.hp = hp
        self.lvl =lvl
    def action(self):
return f"{self,name} ero base action"
kirito = Hero("Kirito", 1000, 100)
 print(kirito.hp)